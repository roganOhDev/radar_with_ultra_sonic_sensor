from utils.log import logger
import random


def get_distance():
    distance = random.randrange(100)

    logger.info(f"Distance From Sensor: {distance}")

    return distance
