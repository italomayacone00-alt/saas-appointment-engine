from flask import Blueprint, render_template
from datetime import datetime, date, time
from ..models import Appointment, db

bp = Blueprint("dashboard", __name__, template_folder="../views/templates")

@bp.route("/")
def index():
    # Definir o início e o fim do dia de hoje para filtrar
    hoje = date.today()
    inicio_dia = datetime.combine(hoje, time.min)
    fim_dia = datetime.combine(hoje, time.max)

    # Buscar todos os agendamentos de HOJE
    agendamentos_hoje = Appointment.query.filter(
        Appointment.start_at >= inicio_dia,
        Appointment.start_at <= fim_dia
    ).order_by(Appointment.start_at.asc()).all()

    # Calcular contagens para os Cards
    count_total = len(agendamentos_hoje)
    
    # Contar quantos estão "scheduled" (Na fila)
    # Nota: Adapte a string se no seu banco você salvou diferente
    count_waiting = sum(1 for a in agendamentos_hoje if a.status == 'scheduled')
    
    # Contar quantos estão "in_service" (Em atendimento)
    count_in_service = sum(1 for a in agendamentos_hoje if a.status == 'in_service')

    return render_template(
        "dashboard.html",
        agendamentos=agendamentos_hoje,
        count_total=count_total,
        count_waiting=count_waiting,
        count_in_service=count_in_service
    )
