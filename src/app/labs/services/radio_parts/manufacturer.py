from app import db
from app.labs.exceptions import ManufacturerNotFoundException
from app.labs.models.radio_parts import Manufacturer


def create_manufacturer(name: str) -> int:
    manufacturer = Manufacturer(name=name)
    db.session.add(manufacturer)
    db.session.commit()
    return manufacturer.id


def get_manufacturer(manufacturer_id: int) -> Manufacturer:
    manufacturer = Manufacturer.query.filter(id=manufacturer_id).first()
    if not Manufacturer:
        raise ManufacturerNotFoundException(f"Manufacturer with ID{manufacturer_id} was not found")
    return manufacturer


def get_all_manufacturers() -> list[Manufacturer]:
    manufacturers = Manufacturer.query.all()
    if not manufacturers:
        raise ManufacturerNotFoundException(f"There are no manufacturers in db")
    return manufacturers
