"""Utility decorator for logging function time"""

import logging
from functools import wraps
from time import time

logging.basicConfig(
    level=logging.DEBUG,
    format=f"%(asctime)s %(levelname)s: %(message)s",
)


def log_time(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        total_time = time() - start_time
        logging.info(f"func:{func.__name__} took: {total_time:.4f} sec")
        return result

    return wrap
