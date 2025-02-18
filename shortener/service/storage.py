import random
import datetime
from queue import Queue
from .key import Key


KEY_LIFETIME = datetime.timedelta(days=1)

container: dict[str: str]
links: set[str]
keys: list[int]
stored: Queue[Key]
inited = False


def init():
    global container
    global keys
    global stored
    global links
    global inited
    container = dict()
    keys = list(range(1048576, 16777216))
    random.shuffle(keys)
    stored = Queue()
    links = set()
    inited = True


def add_link(link: str) -> str | None:
    if link in links:
        return
    key = _generate_key()
    container[key] = link
    return key


def _generate_key() -> str:
    k = keys.pop()
    stored.put(Key(k))
    return hex(k)[2:]


def get_link(short: str) -> str:
    return container[short]


def delete_old_keys():
    if stored.empty():
        return
    while datetime.datetime.now() - stored.queue[0] > KEY_LIFETIME:
        key = stored.get()
        links.remove(container[hex(key.k)[2:]])
        del container[hex(key.k)[2:]]
        keys.append(key.k)
        
