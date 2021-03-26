import os
import logging

name: str = os.getenv("name", "justin")
logging.info(f"Hello, {name}")