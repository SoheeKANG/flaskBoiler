import os
import sys
from flask import Flask
import logging
from typing import Union

PROJECT_ROOT = os.path.abspath(
    ".."
    if os.path.abspath(".").split("/")[-1]
    in [
        "lib",
        "api",
        "helpers",
        "scripts"
        "tests",
       ]
    else "."
)

sys.path.append(PROJECT_ROOT)
logger: Union[logging.Logger, None] = None


def create_app(config: object, mysql_config: object) -> Flask:
    """
    @param config:
    @param mysql_config:
    @return: Flask
    """
    app = Flask(__name__,)

    return app
