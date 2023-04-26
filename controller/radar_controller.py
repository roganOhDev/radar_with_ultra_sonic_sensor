from flask import render_template, Blueprint

bp = Blueprint('radar', __name__)


@bp.route('/radar', methods=['GET'])
def show_radar():
    return render_template('radar.html')
