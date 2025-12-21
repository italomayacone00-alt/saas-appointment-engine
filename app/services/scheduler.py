
from ..models import Appointment
from ..db import db

def slot_available(professional, start_at):
    conflict = Appointment.query.filter_by(professional=professional, start_at=start_at).first()
    return conflict is None

def save_appointment(appt):
    db.session.add(appt)
    db.session.commit()
    return appt
