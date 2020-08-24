import time
import os
import logging
import random

from events import gen_random_event, flush_event

EVENTS_DIR = os.getenv('EVENTS_DIR', './events')
LOGS_DIR = os.getenv('LOGS_DIR', './logs')

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(f'{LOGS_DIR}/{time.strftime("%Y%m%d-%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)

if __name__ == "__main__":
    num_events = 1000
    logging.info(f'Generating {num_events} users')
    for i in range(num_events):
        flush_event(gen_random_event(i), EVENTS_DIR)
    while True:
        time.sleep(1)
