import json
from utils.log import logger
import time
from receiver.ultra_sonic_sensor import get_distance
from const.config import labels
from domain.radar import radar_service

from flask import render_template, Blueprint, Response

bp = Blueprint('radar', __name__, url_prefix='/radar')


@bp.route('/')
def show_radar() -> str:
    return render_template('radar.html')


@bp.route('/data')
def get_data() -> Response:

    return Response(radar_service.get_distance_data_with_stream(), mimetype='text/event-stream')
