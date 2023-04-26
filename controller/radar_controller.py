from flask import render_template, Blueprint, jsonify

bp = Blueprint('radar', __name__)


@bp.route('/radar', methods=['GET'])
def show_radar():
    return render_template('radar.html')


@bp.route('/radar/data')
def get_data():
    data = {
        'labels': ['Eating', 'Drinking', 'Sleeping', 'Designing', 'Coding', 'Cycling', 'Running'],
        'values': [65, 59, 90, 81, 56, 55, 40]
    }
    return jsonify(data)
