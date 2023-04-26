from const.config import max_distance
from utils.log import logger
import random


def get_distance():
    distance = random.randrange(max_distance)

    logger.info(f"Distance From Sensor: {distance}")

    return distance
