from short_url import redis_store
from short_url.utils.number_utils import _10_to_62

REDIS_KEY = 'NUMBER_SENDER'


def get_number():
    return str(_10_to_62(redis_store.incr('REDIS_KEY')))
