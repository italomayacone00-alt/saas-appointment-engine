
from .db import db
from datetime import datetime

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    service_type = db.Column(db.String(80), nullable=False)
    professional = db.Column(db.String(120))
    start_at = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default="scheduled")
<<<<<<< HEAD


# --- ADICIONE ESTA PARTE ABAIXO ---
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    cpf = db.Column(db.String(14)) # Opcional
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
=======
>>>>>>> upstream/main
