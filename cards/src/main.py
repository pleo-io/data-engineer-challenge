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
        logging.FileHandler(
            f'{LOGS_DIR}/{time.strftime("%Y%m%d-%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)

MIN_CYCLE_DELAY = 1
MAX_CYCLE_DELAY = 3
MIN_CYCLE_EVENTS = 5
MAX_CYCLE_EVENTS = 10


def get_id_counter():
    fname = f'{EVENTS_DIR}/__id_counter'
    if not os.path.isfile(fname):
        return 0

    with open(f'{EVENTS_DIR}/__id_counter', 'r') as f:
        return int(f.read())


def flush_id_counter(i):
    fname = f'{EVENTS_DIR}/__id_counter'
    with open(f'{EVENTS_DIR}/__id_counter', 'w') as f:
        f.write(str(i))


if __name__ == "__main__":
    id_counter = get_id_counter()
    while True:
        num_events = random.randrange(MIN_CYCLE_EVENTS, MAX_CYCLE_EVENTS)
        delay_between = random.randrange(MIN_CYCLE_DELAY, MAX_CYCLE_DELAY)
        logging.info(f'Generating {num_events} events')
        for _ in range(num_events):
            flush_event(gen_random_event(id_counter), EVENTS_DIR)
            id_counter = id_counter + 1
        flush_id_counter(id_counter)
        logging.info(f'Sleeping {delay_between} seconds')
        time.sleep(delay_between)
