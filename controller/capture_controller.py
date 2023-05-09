from flask import render_template, Blueprint, Response

from domain.radar import capture_service

bp = Blueprint('capture', __name__, url_prefix='/capture')


@bp.route('/')
def show_capture_list() -> str:
    return render_template('capture_list.html')


@bp.route('/get')
def get_list_data() -> Response:
    return capture_service.find_list()


@bp.route('/<id>')
def show_data(id: int) -> str:
    return render_template('capture.html', id=id)


@bp.route('/<id>/get')
def get_data(id: int) -> Response:
    return capture_service.find(id)
