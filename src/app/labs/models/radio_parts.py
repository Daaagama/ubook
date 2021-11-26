from sqlalchemy.ext.hybrid import hybrid_property

from app import db


class RadioPart(db.Model):
    """
    Model for all the radio parts.
    """
    __tablename__ = "radio_part"
    name = db.Column(db.String(80), nullable=False)
    photo_link = db.Column(db.String(255), nullable=False)
    # transistor_id = db.Column(db.Integer, db.ForeignKey("transistor.id"), nullable=True)
    # capacitor_id = db.Column(db.Integer, db.ForeignKey("capacitor.id"), nullable=True)

    def __repr__(self):
        return f"Radio part {self.name} (id {self.id})"


class Transistor(db.Model):
    __tablename__ = "transistor"
    type = db.Column(db.String(20), nullable=False)


class Capacitor(db.Model):
    __tablename__ = "transistor"
    voltage = db.Column(db.Integer, nullable=False)
