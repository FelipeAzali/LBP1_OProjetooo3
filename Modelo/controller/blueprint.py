from flask import Blueprint, render_template

pagina = Blueprint('pagina', __name__)

@pagina.route('/')
def index():
    return render_template("idex.html")