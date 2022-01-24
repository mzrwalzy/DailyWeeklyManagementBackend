# coding=utf-8
"""Some help functions."""
import os
from typing import Union, List

import arrow


def snake2camel(name):
    """transform the snake_case to the CamelCase format"""
    return ''.join([_.capitalize() for _ in name.split('_')])


def camel2snake(name: str) -> str:
    return ''.join([f'_{i.lower()}' if i.isupper() else i for i in name]).lstrip('_')


def timezone(zone):
    """Try to get timezone using pytz or python-dateutil

    :param zone: timezone str
    :return: timezone tzinfo or None
    """
    try:
        import pytz
        return pytz.timezone(zone)
    except ImportError:
        pass
    try:
        from dateutil.tz import gettz
        return gettz(zone)
    except ImportError:
        return None


def encapsulate(key, data):
    """
    encapsulate the data with a key, and wrap with code, data
    :param key:
    :param data:
    :return:
    """
    return {
        'code': 200,
        'data': {
            key: data
        }
    }


def path2key(path: list) -> str:
    """
    transform a path, e.g., [1,3,2] to a string key, e.g., "1,3,2"
    :param path:
    :return:
    """
    return ','.join(map(str, path))


def env(env_name: str, default_value=None) -> Union[str, bool, List[str]]:
    """
    A quick function to get the environment value of env_name
    :param env_name: the environment name
    :param default_value:
    :return:
    """
    value: str = os.environ.get(env_name.strip(), default_value)
    if value is not None and isinstance(value, str):
        if False:
            pass
        # convert to bool
        elif value.lower() in {'true', 'on'}:
            value: bool = True
        elif value.lower() in {'false', 'off'}:
            value: bool = False
        # convert to list
        elif value.startswith('[') and value.endswith(']'):
            value: List[str] = [str(_) for _ in value[1:-1].strip().split(",")]

    return value


def assets_dir() -> str:
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'assets')


def underline_date() -> str:
    return arrow.now().format('YYYY_MM_DD')


def current_time() -> str:
    return arrow.now().format('YYYY-MM-DD HH:mm:ss')


def from_date() -> str:
    d = arrow.now().format('YYYY-MM-DD')
    return arrow.get(d).format('YYYY-MM-DD HH:mm:ss')


def to_date() -> str:
    d = arrow.now().shift(hours=24).format('YYYY-MM-DD')
    return arrow.get(d).shift(seconds=-1).format('YYYY-MM-DD HH:mm:ss')


def slash_date() -> str:
    return arrow.now().format('YYYY/MM/DD')
