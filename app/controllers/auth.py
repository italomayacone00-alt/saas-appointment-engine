from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint("auth", __name__, template_folder="../views/templates")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Aqui viria a lógica de verificar senha no banco
        # Por enquanto, vamos fingir que deu certo
        return redirect(url_for('dashboard.index'))
    
    return render_template("login.html")

@bp.route("/logout")
def logout():
    # Lógica de logout
    return redirect(url_for('auth.login'))