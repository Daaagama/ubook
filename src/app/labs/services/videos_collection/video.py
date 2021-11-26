from app import db
from app.labs.exceptions import VideoNotFoundException
from app.labs.models.videos_collection import Video
import datetime


def get_video(video_id: int) -> Video:
    """
    Get video from database by it's id if it exists.
    Otherwise, raise ChannelNotFoundException.
    :param video_id: id of video
    :return: Video object
    """
    video = Video.query.filter(Video.id == video_id).first()
    if not video:
        raise VideoNotFoundException(f"Video with ID{video_id} was not found")
    return video


def add_video(title: str, channel_id: int, date_uploaded: datetime.date, video_link: str, preview_link: str) -> int:
    """
    Add new video to database.
    :param title: title of the new video
    :param channel_id: Channel ID to add video to
    :param date_uploaded: datetime.date object represents date the video was added
    :param video_link: link to the youtube video
    :param preview_link: link to the youtube video preview
    :return: ID of new video
    """
    video = Video(title=title,
                  channel_id=channel_id,
                  date_uploaded=date_uploaded,
                  video_link=video_link,
                  preview_link=preview_link)
    db.session.add(video)
    db.session.commit()
    return video.id


def get_last_videos() -> tuple[Video]:
    """
    Get last 9 videos to display on main page
    :return: tuple of 9 last videos
    """
    videos = Video.query.order_by(Video.id.desc()).limit(9).all()
    return videos
