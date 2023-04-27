import datetime
import json

from const.database_config import get_db
from domain.radar.capture import Capture
from utils.time_utils import get_unix_time


def create(distance: [int]):
    distance_json = json.dumps({'data': distance})

    unix_time = get_unix_time(datetime.datetime.now())
    capture = Capture(distance_json, unix_time)

    db = next(get_db())
    db.add(capture)
    db.commit()
