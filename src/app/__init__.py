import os

from flask import Flask, render_template


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

    # Render index.html template for /
    @app.route('/')
    def index():
        return render_template("index.html")

    return app


def register_blueprints(app):
    """
    Put here your blueprints to be registered
    """
    from app.labs.views import lab6
    app.register_blueprint(lab6.bp)


if __name__ == "__main__":
    create_app().run()
