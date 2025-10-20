import uuid
import time


def create_id_user():
    timestamp = int(time.time() * 1000)
    random_part = uuid.uuid4().hex
    return f'user_{timestamp}_{random_part}'