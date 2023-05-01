import json
import time

from const.config import label_size, labels, radar_latency
from domain.radar import capture_repository
from receiver.ultra_sonic_sensor import get_distance
from utils.log import logger


def get_distance_data_with_stream() -> None:
    values = [0] * label_size
    i = 0

    while True:
        try:
            i %= label_size

            json_data = __get_json_data(values, i)

            i += 1
            yield f"data:{json_data}\n\n"

        except Exception as e:
            logger.error(e)

        logger.info(f"Data: {values}")

        time.sleep(radar_latency)


def __get_json_data(values: [int], i: int) -> json:
    new_distance = get_distance()

    values[i] = new_distance

    capture_repository.create(values)

    return json.dumps({'labels': labels, 'values': values})
