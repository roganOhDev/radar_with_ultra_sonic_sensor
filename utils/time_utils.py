import datetime

import time


def get_unix_time(real_datetime: datetime) -> float:
    return time.mktime(real_datetime.timetuple())
