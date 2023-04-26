import json
from utils.log import logger
import time
from receiver.ultra_sonic_sensor import get_distance
from const.config import labels

from flask import render_template, Blueprint, jsonify, Response

bp = Blueprint('radar', __name__, url_prefix='/radar')


@bp.route('/')
def show_radar():
    return render_template('radar.html')


@bp.route('/data')
def get_data1():
    values = [0] * len(labels)

    def stream():
        i = 0

        while True:
            try:
                new_distance = get_distance()

                i %= len(labels)

                values[i] = new_distance
                json_data = json.dumps({'labels': labels, 'values': values})

                i += 1

                yield f"data:{json_data}\n\n"

            except Exception as e:
                logger.error(e)

            logger.info(f"Data: {values}")

            time.sleep(3)

    return Response(stream(), mimetype='text/event-stream')
