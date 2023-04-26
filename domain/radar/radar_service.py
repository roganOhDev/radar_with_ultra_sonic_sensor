import json
import time

from const.config import labels
from receiver.ultra_sonic_sensor import get_distance
from utils.log import logger


def get_distance_data_with_stream() -> None:
    values = [0] * len(labels)
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
