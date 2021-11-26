from sqlalchemy import func, select

from app import db
from app.labs.exceptions import ChannelNotFoundException
from app.labs.models.videos_collection import Channel


def add_channel(name: str, description: str, link: str, subscribers: str, avatar: str) -> int:
    """
    Creates new channel in database
    :param name: name of the channel
    :param description: channel's description
    :param link: link to the channel on youtube
    :param subscribers: number of subscribers
    :param avatar: link to the channel's avatar
    :return: new channel id
    """
    channel = Channel(name=name, subscribers=subscribers, description=description, link=link, avatar=avatar)
    db.session.add(channel)
    db.session.commit()
    return channel.id


def get_channel(channel_id: int) -> Channel:
    """
    Get channel from database by it's id if channel exists.
    Otherwise, raise ChannelNotFoundException.
    :param channel_id: channel id
    :return: Channel
    """
    channel = Channel.query.filter(id=channel_id).first()
    if not channel:
        raise ChannelNotFoundException(f"Channel with ID{channel_id} was not found")
    return channel


def channels_search_by_name(channel_name: str) -> Channel:
    """
    Search for channel in database. Return Channel in case it was found.
    Otherwise, raise ChannelNotFoundException.
    :param channel_name: [part of] the channel name
    :return: Channel
    """
    channels = Channel.query.filter(func.lower(Channel.name).contains(func.lower(channel_name))).all()
    if not channels:
        raise ChannelNotFoundException(f"Channel with name {channel_name} was not found")
    return channels


def get_channel_by_id(channel_id: int) -> Channel:
    channel = Channel.query.filter(Channel.id == channel_id).first()
    if not channel:
        raise ChannelNotFoundException(f"Channel with id {channel_id} was not found")
    return channel


def get_all_channels() -> list[Channel]:
    """
    Return all channels in db if there are any.
    Otherwise, raise ChannelNotFoundException.
    :return: Channel
    """
    channels = Channel.query.all()
    if not channels:
        raise ChannelNotFoundException(f"There are no channels in db")
    return channels
