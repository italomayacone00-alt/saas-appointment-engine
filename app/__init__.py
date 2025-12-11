
from flask import Flask
from .db import init_db
from .config import SECRET_KEY, SQLALCHEMY_DATABASE_URI

from .controllers.appointments import bp as appointments_bp
from .controllers.auth import bp as auth_bp
from .controllers.dashboard import bp as dashboard_bp
<<<<<<< HEAD
from .controllers.patients import bp as patients_bp # <--- ADICIONE ESTE IMPORT
=======
>>>>>>> upstream/main

def create_app():
    app = Flask(__name__, template_folder="views/templates")
    app.config.update(
        SECRET_KEY=SECRET_KEY,
        SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI,
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    init_db(app)
    app.register_blueprint(appointments_bp, url_prefix="/appointments")

<<<<<<< HEAD
    # Rota do Dashboard (FALTAVA ESSA LINHA)
    # O url_prefix="/" significa que ela será a página inicial
    app.register_blueprint(dashboard_bp, url_prefix="/")
    app.register_blueprint(patients_bp, url_prefix="/patients")

    # Rota de Autenticação (FALTAVA ESSA TAMBÉM)
    # Vi que você importou o auth_bp, então já deixei registrado para quando você usar login
    app.register_blueprint(auth_bp, url_prefix="/auth")

=======
>>>>>>> upstream/main
    @app.route("/health")
    def health():
        return {"status": "ok"}
    return app
