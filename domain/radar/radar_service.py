import json
import time

from const.config import label_size, labels, radar_latency
from domain.radar import capture_repository
from receiver.ultra_sonic_sensor import get_distance
from utils.log import logger


def get_distance_data_with_stream() -> None:
    values = [0] * label_size
    i_increase = True
    i = 0

    while True:
        try:
            i, i_increase = __get_label_num(i, i_increase)

            json_data = __get_json_data(values, i)

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


def __get_label_num(before_label_value: int, i_increase: bool) -> (int, int):
    label_value: int

    if i_increase:
        label_value = before_label_value + 1
        if label_value == label_size:
            i_increase = False
            label_value = before_label_value - 1

    else:
        label_value = before_label_value - 1
        if label_value < 0:
            i_increase = True
            label_value = before_label_value + 1

    return label_value, i_increase
