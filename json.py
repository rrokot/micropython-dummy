from ujson import *
from ujson import dumps as original_dumps


def dumps(*args, **kwargs):
    kwargs.pop('indent', None)
    return original_dumps(*args, **kwargs)
