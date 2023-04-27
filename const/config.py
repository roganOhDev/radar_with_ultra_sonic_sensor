from enum import Enum

angle = 0
label_size = 10
labels = []
while angle < 360:
    labels.append(str(angle) + " degree")
    angle += 360 / label_size

max_distance = 100
db_name = "test.db"


class RunVersion(Enum):
    debug = "DEBUG"
    demo = "DEMO"


# version = RunVersion.debug
version = RunVersion.demo
