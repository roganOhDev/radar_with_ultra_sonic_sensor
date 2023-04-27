from flask import jsonify

from domain.radar import capture_repository
from utils.time_utils import get_date_time


def get_list():
    list = capture_repository.get_all()

    data = __get_real_dates(list)

    return jsonify(data)


def __get_real_dates(values):
    real_dates = []
    ids = []
    for value in values:
        ids.append(str(value.id))
        real_dates.append(str(get_date_time(value.created_at)))

    return {
        'ids': ids,
        'values': real_dates
    }
