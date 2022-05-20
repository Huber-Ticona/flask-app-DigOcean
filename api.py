from flask import Blueprint, render_template

api_bp = Blueprint('api_bp', __name__, static_folder='static', template_folder='templates')

@api_bp.route('/productos')
def productos():
    return "<p>hola productos<p>"