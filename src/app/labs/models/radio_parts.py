from app import db


class Manufacturer(db.Model):
    __tablename = "manufacturer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


class RadioPart(db.Model):
    """
    Model for all the radio parts.
    """
    __tablename__ = "radio_part"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))
    manufacturer = db.relationship("Manufacturer", backref="radio_parts")
    type = db.Column(db.String(50), nullable=False)
    package = db.Column(db.String(20), nullable=True)
    photo_link = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Radio part {self.name} (id {self.id})"


class Transistor(db.Model):
    __tablename__ = "transistor"
    id = db.Column(db.Integer, primary_key=True)
    radiopart_id = db.Column(db.Integer, db.ForeignKey('radio_part.id'))
    radiopart = db.relationship("RadioPart", backref=db.backref("transistor", uselist=False))
    type = db.Column(db.String(40), nullable=False)
    power_dissipation = db.Column(db.Float, nullable=False)
    voltage = db.Column(db.Float, nullable=False)
    current = db.Column(db.Float, nullable=False)
    temp = db.Column(db.Float, nullable=False)


class Capacitor(db.Model):
    __tablename__ = "capacitor"
    id = db.Column(db.Integer, primary_key=True)
    radiopart_id = db.Column(db.Integer, db.ForeignKey('radio_part.id'))
    radiopart = db.relationship("RadioPart", backref=db.backref("capacitor", uselist=False))
    voltage = db.Column(db.Float, nullable=False)
    capacity = db.Column(db.Float, nullable=False)


class Resistor(db.Model):
    __tablename__ = "resistor"
    id = db.Column(db.Integer, primary_key=True)
    radiopart_id = db.Column(db.Integer, db.ForeignKey('radio_part.id'))
    radiopart = db.relationship("RadioPart", backref=db.backref("resistor", uselist=False))
    power_dissipation = db.Column(db.Float, nullable=False)
    resistance = db.Column(db.Float, nullable=False)


class PowerUnit(db.Model):
    __tablename__ = "power_unit"
    id = db.Column(db.Integer, primary_key=True)
    radiopart_id = db.Column(db.Integer, db.ForeignKey('radio_part.id'))
    radiopart = db.relationship("RadioPart", backref=db.backref("power_unit", uselist=False))
    input_voltage = db.Column(db.Float, nullable=False)
    output_voltage = db.Column(db.Float, nullable=False)
    output_current = db.Column(db.Float, nullable=False)
    power = db.Column(db.Float, nullable=False)
