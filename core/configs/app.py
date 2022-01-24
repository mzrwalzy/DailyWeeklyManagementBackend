from pathlib import Path
from typing import List

from core.utils import env

PROJECT_PATH: Path = (Path(__file__) / '../../../').resolve()
PROJECT_NAME: str = env("PROJECT_NAME", "A demo app")

# CORSMiddleware
ALLOW_ORIGINS: List[str] = env('ALLOW_ORIGINS', ['*'])
ALLOW_CREDENTIALS: bool = env('ALLOW_CREDENTIALS', True)
ALLOW_METHODS: List[str] = env('ALLOW_METHODS', ['*'])
ALLOW_HEADERS: List[str] = env('ALLOW_HEADERS', ['*'])

if __name__ == '__main__':
    __all = globals()
    envs = {k: __all[k] for k in __all if k.isupper()}
    for k in envs:
        v = __all[k]
        print(f'{k}={v} ({type(v)})')
