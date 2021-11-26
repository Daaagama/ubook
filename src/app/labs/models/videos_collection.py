from app import db


class Channel(db.Model):
    __tablename__ = "channel"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.UnicodeText, nullable=True)
    link = db.Column(db.String(255), nullable=False)
    subscribers = db.Column(db.String(20), nullable=False)
    avatar = db.Column(db.String(255), nullable=True)

    def __str__(self):
        return f"Channel '{self.name}'({self.link}), ID={self.id}"


class Video(db.Model):
    __tablename__ = "video"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'))
    channel = db.relationship("Channel", backref="videos")
    date_uploaded = db.Column(db.Date, nullable=False)
    video_link = db.Column(db.String(255), nullable=False)
    preview_link = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return f"Video '{self.title}', ID={self.id}"
