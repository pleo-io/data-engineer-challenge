import datetime
import os
import uuid
import time
import json
import logging
import random
from faker import Faker

fake = Faker()
Faker.seed(1001)

def __gen_metadata():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {
        'type': 'user', 
        'event_at': now,
        'event_id': str(uuid.uuid4())
    }

def __gen_new_user(i):
    event = {}
    event['metadata'] = __gen_metadata()

    event['payload'] = {
        'id': i,
        'name': fake.name(),
        'address': fake.address(),
        'job': fake.job(),
        'score': random.random()
    }

    return event

def gen_random_event(i):
    return __gen_new_user(i)

def flush_event(event, filedir):
    fname = f"{filedir}/{event['metadata']['event_id']}.json"
    if not os.path.isfile(fname):
        try:
            data = json.dumps(event)
            with open(fname, 'w') as f:
                json.dump(event, f, indent = 2)
                logging.debug(f'Flushed event to {fname}')
        except:
            logging.error(f'Failed to flush event to {fname}: {event}')
