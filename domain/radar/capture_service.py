import json

from flask import jsonify

from const.config import labels
from domain.radar import capture_repository
from utils.time_utils import get_date_time


def find_list():
    list = capture_repository.get_all()

    data = __reformat_for_find_all(list)

    return jsonify(data)


def find(id: int):
    capture_value = capture_repository.find(id)

    data = __reformat_for_find(capture_value[0])

    return jsonify(data)


def __reformat_for_find_all(values):
    real_dates = []
    ids = []
    for value in values:
        ids.append(str(value.id))
        real_dates.append(str(get_date_time(value.created_at)))

    return {
        'ids': ids,
        'dates': real_dates
    }


def __reformat_for_find(value):
    value_list = []

    data_values = json.loads(value)['data']

    for i in range(len(data_values)):
        value_list.append(str(data_values[i]))

    return {
        "labels": labels,
        "values": value_list
    }
