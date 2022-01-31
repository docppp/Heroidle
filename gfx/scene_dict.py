from collections.abc import MutableMapping


class SceneDict(MutableMapping):

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))
        if 'start_pos' in self.store:
            SceneDict.make_details_relative(self.store['start_pos'], self.store['details'])
        if 'restorable' in self.store:
            self.backup_pos = SceneDict.save_details_pos(self.store['details'])

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def restore(self):
        if 'restorable' in self.store:
            for detail in self.store['details']:
                detail.set_pos(self.backup_pos[id(detail)])
            return self
        else:
            raise KeyError("Cannot restore scene without specifying 'restorable' key as True")

    @staticmethod
    def make_details_relative(start_pos: tuple[int, int], details: list):
        for detail in details:
            detail.change_pos_by(start_pos)

    @staticmethod
    def save_details_pos(details: list):
        positions = {}
        for detail in details:
            positions[id(detail)] = (detail.x, detail.y)
        return positions


