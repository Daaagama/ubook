import datetime

from flask import Blueprint, render_template, request, flash, url_for, redirect

# URL prefix for routes in this file
bp = Blueprint('lab6', __name__, url_prefix="/labs/lab6")


@bp.route("/", methods=["GET"])
def lab6_feedback_form():
    """
    View for feedback form
    """
    return render_template("labs/lab6/feedback-form.html", title="Feedback form")


@bp.route("/", methods=["POST"])
def lab6_form_handler():
    """
    Handler for feedback form.
    Receives *email* and *message* from POST request.
    Return filled feedback-handler.html if email and message are not empty
    """
    email = request.form.get("email")
    message = request.form.get("message")
    if email and message:
        return render_template("labs/lab6/feedback-handler.html", email=email, message=message,
                               date=datetime.date.today().strftime("%d.%m.%Y"))
    else:
        flash("Введіть адресу електронної скриньки та повідомлення", "danger")
        return redirect(url_for("lab6.lab6_feedback_form"))
