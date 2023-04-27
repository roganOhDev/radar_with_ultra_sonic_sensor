from enum import Enum

labels = ['Eating', 'Drinking', 'Sleeping', 'Designing', 'Coding', 'Cycling', 'Running']
max_distance = 100
db_name = "test.db"


class RunVersion(Enum):
    debug = "DEBUG"
    demo = "DEMO"


version = RunVersion.debug
# version = RunVersion.demo
