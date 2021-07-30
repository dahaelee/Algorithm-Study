class MapSum:

    def __init__(self):
        self.map = dict()

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        return sum(self.map[key] for key in self.map if key.startswith(prefix))
