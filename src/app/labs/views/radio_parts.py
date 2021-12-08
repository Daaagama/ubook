from flask import Blueprint, render_template, flash, request, redirect, url_for

from app.labs.exceptions import ManufacturerNotFoundException, WebApplicationBaseException, RadioPartNotFoundException
from app.labs.services.radio_parts.manufacturer import create_manufacturer, get_all_manufacturers
from app.labs.services.radio_parts.radio_part import create_radio_part, create_transistor, create_capacitor, \
    create_resistor, create_power_unit, get_part, search_parts_by_name

bp = Blueprint('radio_parts', __name__, url_prefix="/radio")


@bp.route("/", methods=["GET"])
def index():
    q = request.args.get("q") or ""
    parts = []
    if q:
        try:
            parts = search_parts_by_name(q)
        except RadioPartNotFoundException:
            parts = []
    return render_template("labs/radio_parts/index.html", title="Довідник з радіотехніки", q=q, radioparts=parts)


@bp.route("/create-manufacturer", methods=["POST"])
def create_manufacturer_handler():
    name = request.form.get("name")
    if not name:
        flash("Ви повинні ввести назву компанії виробника", "warning")
    else:
        flash("Додано нового виробника", "success")
        create_manufacturer(name)

    return redirect(request.referrer)


@bp.route("/create-radio-part", methods=["GET"])
def create_radio_part_view():
    radiopart_type = request.args.get("radiopart_type") or 1
    print(dict(request.args))
    try:
        radiopart_type = int(radiopart_type)
    except ValueError:
        radiopart_type = 1
    radiopart_type_names = {
        1: ("Транзистор", "transistor.html"),
        2: ("Конденсатор", "capacitor.html"),
        3: ("Резистор", "resistor.html"),
        4: ("Блок живлення", "power-unit.html"),
    }

    try:
        manufacturers = get_all_manufacturers()
    except ManufacturerNotFoundException:
        manufacturers = []
    return render_template("labs/radio_parts/new-radio-part.html", radiopart_name=radiopart_type_names[radiopart_type][0], radiopart_filename=radiopart_type_names[radiopart_type][1], manufacturers=manufacturers, radiopart_type=radiopart_type)


@bp.route("/create-radio-part", methods=["POST"])
def create_radio_part_handler():
    args = dict(request.form)
    args["radiopart_type"] = request.args.get("radiopart_type")
    print(args)

    if not {"name", "package", "photo_link", "manufacturer"}.issubset(args):
        flash("Заповніть всі поля та спробуйте ще раз", "danger")
        return redirect(url_for("radio_parts.create_radio_part_view", radiopart_type=args["radiopart_type"]))
    radio_part_id = -1

    try:
        radio_part_id = create_radio_part(name=args["name"],
                                          manufacturer_id=int(args["manufacturer"]),
                                          _type=args["radiopart_type"],
                                          package=args["package"],
                                          photo_url=args["photo_link"])
        if args["radiopart_type"] == "1" and {"transistor_type", "power_dissipation", "voltage", "current", "temp"}.issubset(args):
            create_transistor(radio_part_id=radio_part_id,
                              _type=args["transistor_type"],
                              power_dissipation=float(args["power_dissipation"]),
                              voltage=float(args["voltage"]),
                              current=float(args["current"]),
                              temp=float(args["temp"]))
        elif args["radiopart_type"] == "2" and {"voltage", "capacity"}.issubset(args):
            create_capacitor(radio_part_id=radio_part_id,
                             voltage=float(args["voltage"]),
                             capacity=float(args["capacity"]))
        elif args["radiopart_type"] == "3" and {"power_dissipation", "resistance"}.issubset(args):
            create_resistor(radio_part_id=radio_part_id,
                            power_dissipation=float(args["power_dissipation"]),
                            resistance=float(args["resistance"]))
        elif args["radiopart_type"] == "4" and {"input_voltage", "output_voltage", "output_current", "power"}.issubset(args):
            create_power_unit(radio_part_id=radio_part_id,
                              input_voltage=float(args["input_voltage"]),
                              output_voltage=float(args["output_voltage"]),
                              output_current=float(args["output_current"]),
                              max_power=float(args["power"]))
        else:
            flash("Ви повинні заповнити всі обов'язкові поля", "danger")
            return redirect(url_for("radio_parts.create_radio_part_view"))

    except (WebApplicationBaseException, ValueError):
        if radio_part_id != -1:
            # remove radio_part from db
            ...
        flash("Ви повинні заповнити всі обов'язкові поля", "danger")
        return redirect(url_for("radio_parts.create_radio_part_view"))

    else:
        flash("Радіодеталь додано", "success")
        return redirect(url_for("radio_parts.index"))


@bp.route("radiopart/<radiopart_id>", methods=["GET"])
def part_info(radiopart_id):
    try:
        radiopart = get_part(radiopart_id)
    except RadioPartNotFoundException:
        flash("Виникла помилка: радіодеталь не знайдено", "warning")
        return redirect(url_for("radio_parts.index"))
    return render_template("labs/radio_parts/radio-part-info.html", radiopart=radiopart)
