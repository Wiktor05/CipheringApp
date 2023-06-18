class Buffer:
    """
    "ROT47": ["...", "..."],
    "ROT13": ["...", "..."]
    """

    def __init__(self):
        self.storage = {"rot47": [], "rot13": []}

    def insert(self, key, text):
        key = key.lower()
        self.storage[key].append(text)

    def clear(self):
        self.storage = {"rot47": [], "rot13": []}
