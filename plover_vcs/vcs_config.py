from typing import List


class VcsConfig:
    def __init__(self, vcs: str = "", dictionaries: List[str] = None):
        self.__vcs = vcs
        self.__dictionaries = [] if dictionaries is None else dictionaries

    @property
    def vcs(self):
        return self.__vcs

    @vcs.setter
    def vcs(self, vcs: str):
        self.__vcs = vcs

    @property
    def dictionaries(self):
        return self.__dictionaries

    @dictionaries.setter
    def dictionaries(self, dictionaries):
        self.dictionaries = dictionaries
