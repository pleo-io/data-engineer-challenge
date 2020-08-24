import uuid
import time
import json
import logging
import random
import datetime
from faker import Faker

fake = Faker()
Faker.seed(1001)

card_cache = {}

def __gen_metadata():
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {
        'type': 'card', 
        'event_at': now,
        'event_id': str(uuid.uuid4())
    }

def __gen_new_card(i):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    payload = {
        'id': i,
        'user_id': random.randint(0, 1000),
        'created_by_name': fake.name(),
        'updated_at': now,
        'created_at': now,
        'active': random.choice([True, False])
    }

    event = {
        'payload': payload,
        'metadata': __gen_metadata()
    }
    card_cache[event['payload']['id']] = event

    return event

def __gen_modify_card(active):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    event = random.choice(list(card_cache.values()))
    event['payload']['updated_at'] = now
    event['payload']['active'] = active
    event['metadata'] = __gen_metadata()

    card_cache[event['payload']['id']] = event

    return event

def __gen_missing_key_event(i):
    event = __gen_new_card(i)
    del event['payload']['user_id']
    return event

def gen_random_event(i):
    if len(card_cache) == 0:
        return __gen_new_card(i)

    roll = random.randrange(100)

    if roll < 40:
        return __gen_new_card(i)
    elif roll < 45:
        return __gen_missing_key_event(i)
    else:
        return __gen_modify_card(random.choice([True, False]))

def flush_event(event, filedir):
    fname = f"{filedir}/{event['metadata']['event_id']}.json"
    try:
        data = json.dumps(event)
        with open(fname, 'w') as f:
            json.dump(event, f, indent = 2)
            logging.debug(f'Flushed event to {fname}')
    except:
        logging.error(f'Failed to flush event to {fname}: {event}')
