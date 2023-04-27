from flask import render_template, Blueprint, Response, jsonify

from const.config import labels

bp = Blueprint('capture', __name__, url_prefix='/capture')


@bp.route('/')
def show_capture_list() -> str:
    return render_template('capture_list.html')


@bp.route('/get')
def get_list_data() -> Response:
    data = {
        'values': [65, 59, 90, 81, 56, 55, 40]
    }

    return jsonify(data)


@bp.route('/<id>')
def show_data(id: int) -> str:
    return render_template('capture.html', id=id)


@bp.route('/<id>/get')
def get_data(id: int) -> Response:
    data = {
        'labels': labels,
        'values': [65, 59, 90, 81, 56, 55, 40]
    }

    return jsonify(data)
