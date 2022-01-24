import typing as tp
from importlib import import_module
from pathlib import Path

from core.resources._base import BaseResource

AVAILABLE_RESOURCES: tp.List[BaseResource] = []
for f in (Path(__file__).parent.glob('*.py')):
    if not f.name.startswith('_') and f.is_file():
        module = import_module(f'.{f.stem}', __package__)

        try:
            AVAILABLE_RESOURCES.append(module.resource)
        except:  # noqa: E722 do not use bare 'except'
            pass


# from core.resources.address import AddressResource
#
# AVAILABLE_RESOURCES = [
#     AddressResource,
# ]


def register_resources(app):
    for resource in AVAILABLE_RESOURCES:
        app.include_router(resource.router)
