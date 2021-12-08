import os
from datetime import datetime

from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # Load secret key from environment variable
        app.secret_key = os.environ.get("UBOOK_SECRET_KEY")
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    register_blueprints(app)
    db_setup(app)

    # Render index.html template for /
    @app.route('/')
    def index():
        return render_template("index.html")

    return app


def register_blueprints(flask_app):
    """
    Put here your blueprints to be registered
    """
    from app.labs.views import lab6, videos_collection, radio_parts
    flask_app.register_blueprint(lab6.bp)
    flask_app.register_blueprint(videos_collection.bp)
    flask_app.register_blueprint(radio_parts.bp)


def db_setup(flask_app):
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
    db.init_app(flask_app)
    migrate.init_app(flask_app, db)


if __name__ == "__main__":
    app = create_app()
    app.app_context().push()
    app.run()
