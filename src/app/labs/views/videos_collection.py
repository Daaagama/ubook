from datetime import datetime

from flask import Blueprint, render_template, request, flash, redirect, url_for

from app.labs.services.videos_collection.video import add_video, get_video, get_last_videos
from app.labs.exceptions import ChannelNotFoundException
from app.labs.services.videos_collection.channel import channels_search_by_name, get_channel_by_id, add_channel, \
    get_all_channels

bp = Blueprint('videos_collection', __name__, url_prefix="/videos")


@bp.route("/", methods=["GET"])
def videos_collection_main_page():
    last_videos = get_last_videos()
    return render_template("labs/videos_collection/index.html", title="Колекція відео", videos=last_videos)


@bp.route("search", methods=["GET"])
def videos_search_page():
    q = request.args.get("q")
    try:
        channels = channels_search_by_name(q)
    except ChannelNotFoundException:
        channels = []
    return render_template("labs/videos_collection/search.html", title="Пошук", q=q, channels=channels)


@bp.route("channel/<channel_id>", methods=["GET"])
def channel_info_page(channel_id):
    try:
        channel = get_channel_by_id(channel_id)
    except ChannelNotFoundException:
        flash("Виникла помилка: канал не знайдено", "warning")
        return redirect(url_for("videos_collection.videos_collection_main_page"))
    return render_template("labs/videos_collection/channel-info.html", channel=channel)


@bp.route("new_channel", methods=["GET"])
def new_channel():
    return render_template("labs/videos_collection/channel-new.html")


@bp.route("new_channel", methods=["POST"])
def new_channel_handler():
    name = request.form.get("name")
    description = request.form.get("description") or ""
    link = request.form.get("link")
    subscribers = request.form.get("subscribers")
    avatar = request.form.get("avatar") or ""

    if not (name or link or subscribers):
        flash("Ви повинні заповнити всі обов'язкові поля", "warning")
        return render_template("labs/videos_collection/channel-new.html")

    channel_id = add_channel(name, description, link, subscribers, avatar)
    return redirect(url_for("videos_collection.channel_info_page", channel_id=channel_id))


@bp.route("new_video", methods=["GET"])
def new_video():
    try:
        channels = get_all_channels()
    except ChannelNotFoundException:
        channels = []
    return render_template("labs/videos_collection/video-new.html", title="Створити нове відео", channels=channels)


@bp.route("new_video", methods=["POST"])
def new_video_handler():
    title = request.form.get("title")
    date = datetime.strptime(request.form.get("date"), "%Y-%m-%d").date()
    preview_link = request.form.get("preview_link")
    video_link = request.form.get("video_link")
    channel_id = request.form.get("channel")

    if not (title or date or preview_link or video_link or channel_id) or not channel_id.isnumeric():
        flash("Ви повинні заповнити всі поля", "warning")
        return render_template("labs/videos_collection/channel-new.html")

    video_id = add_video(title=title, channel_id=int(channel_id), date_uploaded=date, video_link=video_link, preview_link=preview_link)
    return redirect(url_for("videos_collection.video_info_page", video_id=video_id))


@bp.route("video/<video_id>", methods=["GET"])
def video_info_page(video_id):
    try:
        video = get_video(video_id)
    except ChannelNotFoundException:
        flash("Виникла помилка: канал не знайдено", "warning")
        return redirect(url_for("videos_collection.videos_collection_main_page"))
    return render_template("labs/videos_collection/video-info.html", title=video.title, video=video)
