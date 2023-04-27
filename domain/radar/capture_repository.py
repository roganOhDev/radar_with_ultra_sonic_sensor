import datetime
import json

from sqlalchemy import select

from const.database_config import get_db
from domain.radar.capture import Capture
from utils.time_utils import get_unix_time


def create(distance: [int]):
    distance_json = json.dumps({'data': distance})

    unix_time = get_unix_time(datetime.datetime.now())
    Capture(distance_json, unix_time).save()


def get_all() -> [int]:
    db = next(get_db())
    stmt = select(Capture.id, Capture.created_at)
    return db.execute(stmt).fetchall()
