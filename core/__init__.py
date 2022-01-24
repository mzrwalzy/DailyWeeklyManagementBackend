# coding=utf-8
"""The app package, containing the app factory function."""

import dotenv

dotenv.load_dotenv()

from core.main import create_app  # noqa: E402 module level import not at top of file
