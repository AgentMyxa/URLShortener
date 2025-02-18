import datetime

class Key:
    k: int
    creation_time: datetime.datetime

    def __init__(self, key: int):
        self.k = key
        self.creation_time = datetime.datetime.now()