from const.config import port, baudrate, timeout
import serial

from utils.log import logger

coms = serial.Serial(port, baudrate=baudrate, timeout=timeout)


def get_distance() -> int:
    clear_serial_buffer()

    distance = int(float(coms.readline().decode('utf-8').strip()))
    logger.info(f"distance: {distance}")

    if distance >= 100:
        return 100
    else:
        return distance


def clear_serial_buffer():
    while coms.in_waiting > 0:
        _ = coms.readline()
