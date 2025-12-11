from flask import Blueprint, render_template

from ..models import Appointment 

bp = Blueprint("dashboard", __name__, template_folder="../views/templates")

@bp.route("/")
def index():
    # Exemplo: Mostrar quantos agendamentos existem hoje
    total_agendamentos = Appointment.query.count()
    return render_template("dashboard.html", total=total_agendamentos)