from typing import List


class LineChanges:
    def __init__(self, added: List[str] = None, deleted: List[str] = None):
        self.__added = [] if added is None else added
        self.__deleted = [] if deleted is None else deleted

    @property
    def added(self) -> List[str]:
        return self.__added

    @added.setter
    def added(self, added: List[str]):
        self.__added = added

    @property
    def deleted(self) -> List[str]:
        return self.__deleted

    @deleted.setter
    def deleted(self, deleted: List[str]):
        self.__deleted = deleted

