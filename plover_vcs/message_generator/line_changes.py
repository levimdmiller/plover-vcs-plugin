from typing import List


class LineChanges():
    def __init__(self, added: List[str] = None, deleted: List[str] = None):
        self.__added = [] if added is None else added
        self.__deleted = [] if deleted is None else deleted

    @property
    def added(self):
        return self.__added

    @added.setter
    def added(self, added):
        self.__added = added

    @property
    def deleted(self):
        return self.__deleted

    @deleted.setter
    def deleted(self, deleted):
        self.__deleted = deleted

