from flask import Blueprint, request, jsonify, render_template
from datetime import datetime
from ..models import Appointment
from ..services.scheduler import slot_available, save_appointment

bp = Blueprint("appointments", __name__, template_folder="../views/templates")

@bp.route("/", methods=["GET"])
def list_view():
    items = Appointment.query.order_by(Appointment.start_at).all()
    return render_template("appointments.html", appointments=items)

@bp.route("/create", methods=["POST"])
def create():
    data = request.get_json() or {}
    name = data.get("name")
    service_type = data.get("service_type")
    professional = data.get("professional")
    start_at = data.get("start_at")

    if not (name and service_type and start_at):
        return {"error":"missing fields"}, 400

    start_dt = datetime.fromisoformat(start_at)

    if not slot_available(professional, start_dt):
        return {"error":"slot busy"}, 409

    appt = Appointment(name=name, service_type=service_type, professional=professional, start_at=start_dt)
    save_appointment(appt)
    return {"id": appt.id}, 201
