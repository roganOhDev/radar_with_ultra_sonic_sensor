from const.config import max_distance
from utils.log import logger
import serial

coms = serial.Serial("COM3",baudrate=9600,timeout=0.001)

def get_distance():
    distance=coms.readline().decode().strip()
    print(distance)
    logger.info(f"Distance From Sensor: {distance}")    
    return  distance
