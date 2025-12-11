
from flask import Flask
from .db import init_db
from .config import SECRET_KEY, SQLALCHEMY_DATABASE_URI

from .controllers.appointments import bp as appointments_bp
from .controllers.auth import bp as auth_bp
from .controllers.dashboard import bp as dashboard_bp

def create_app():
    app = Flask(__name__, template_folder="views/templates")
    app.config.update(
        SECRET_KEY=SECRET_KEY,
        SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI,
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    init_db(app)
    app.register_blueprint(appointments_bp, url_prefix="/appointments")

    @app.route("/health")
    def health():
        return {"status": "ok"}
    return app
