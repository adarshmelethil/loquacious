#!/usr/bin/env python3
"""loquacious

Usage:
  loquacious hello [--log-level=<level>]
  loquacious talk [--log-level=<level>]
  loquacious (-h | --help)
  loquacious --version

Options:
  -h --help            Show this screen.
  --version            Show version.
  --log-level=<level>  Logging level verbosity [default: info].

"""
import logging
import json
import requests
from typing import Callable

from docopt import docopt


def setup_logger(level_name):
    level = logging.getLevelName(level_name.upper())
    logging.basicConfig(
        level=level, format="%(name)s - %(levelname)s - %(message)s",
    )


def talk(**kwargs):
    api_key = "048462d8-aad8-4e3c-86c4-31a526b95141"

    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={"text": "full moon 🌕"},
        headers={"api-key": api_key},
    )
    data = r.json()
    print(data["output"])


def hello(**kwargs):
    logging.info("hello")
    logging.info(f"kwargs: {json.dumps(kwargs, indent=2)}")


def main():
    args = docopt(__doc__, version="Naval Fate 2.0")
    setup_logger(args["--log-level"])

    for func_name, func in filter(
        lambda kv: isinstance(kv[1], Callable), globals().items()
    ):
        if func_name in args and args[func_name]:
            func(**args)
