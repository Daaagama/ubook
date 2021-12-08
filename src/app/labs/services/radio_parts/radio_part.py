from sqlalchemy import func

from app import db
from app.labs.exceptions import RadioPartNotFoundException
from app.labs.models.radio_parts import RadioPart, Transistor, Capacitor, Resistor, PowerUnit


def get_part(radio_part_id: int) -> RadioPart:
    part = RadioPart.query.filter(RadioPart.id == radio_part_id).first()
    if not part:
        raise RadioPartNotFoundException(f"Radio part with ID{radio_part_id} was not found")
    bool
    return part


def search_parts_by_name(name: str) -> list[RadioPart]:
    parts = RadioPart.query.filter(func.lower(RadioPart.name).contains(func.lower(name))).all()
    if not parts:
        raise RadioPartNotFoundException(f"Radio part with name {name} was not found")
    return parts


def create_radio_part(name: str, manufacturer_id: int, _type: str, package: str, photo_url: str) -> int:
    part = RadioPart(name=name, manufacturer_id=manufacturer_id, type=_type, package=package, photo_link=photo_url)
    db.session.add(part)
    db.session.commit()
    return part.id


def create_transistor(radio_part_id: int, _type: str, power_dissipation: float, voltage: float, current: float, temp: float) -> int:
    transistor = Transistor(radiopart_id=radio_part_id, type=_type, power_dissipation=power_dissipation, voltage=voltage, current=current, temp=temp)
    db.session.add(transistor)
    db.session.commit()
    return transistor.id


def create_capacitor(radio_part_id: int, voltage: float, capacity: float) -> int:
    capacitor = Capacitor(radiopart_id=radio_part_id, voltage=voltage, capacity=capacity)
    db.session.add(capacitor)
    db.session.commit()
    return capacitor.id


def create_resistor(radio_part_id: int, power_dissipation: float, resistance: float) -> int:
    resistor = Resistor(radiopart_id=radio_part_id, power_dissipation=power_dissipation, resistance=resistance)
    db.session.add(resistor)
    db.session.commit()
    return resistor.id


def create_power_unit(radio_part_id: int, input_voltage: float, output_voltage: float, output_current: float, max_power: float) -> int:
    power_unit = PowerUnit(radiopart_id=radio_part_id, input_voltage=input_voltage, output_voltage=output_voltage, output_current=output_current, power=max_power)
    db.session.add(power_unit)
    db.session.commit()
    return power_unit.id
