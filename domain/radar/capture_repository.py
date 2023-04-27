import datetime
import json

from sqlalchemy import select

from const.config import label_size
from const.database_config import get_db
from domain.radar.capture import Capture
from utils.log import logger
from utils.time_utils import get_unix_time


def create(distance: [int]):
    distance_json = json.dumps({'data': distance})

    unix_time = get_unix_time(datetime.datetime.now())
    Capture(distance_json, unix_time).save()


def get_all() -> [int]:
    db = next(get_db())
    stmt = select(Capture.id, Capture.created_at).order_by(Capture.id.desc())
    return db.execute(stmt).fetchall()

def find(id: int):
    db = next(get_db())
    stmt = select(Capture.data).where(Capture.id == id)
    capture = db.execute(stmt).fetchone()

    if capture is None:
        logger.error("Capture is Not Found, ID : " + str(id))
        default_values = [0] * label_size
        return (default_values, )

    return capture

