from const.config import port, baudrate, timeout
from utils.log import logger
import serial

coms = serial.Serial(port, baudrate=baudrate, timeout=timeout)


def get_distance():
    distance = coms.readline().decode().strip()
    print(distance)
    logger.info(f"Distance From Sensor: {distance}")
    return distance
