import json
import os
from typing import List
from plover.config import CONFIG_DIR


# Config path.
CONFIG_FILE = os.path.join(CONFIG_DIR, 'plover_vcs.json')


class VcsConfig:
    def __init__(self, vcs: str = "", dictionaries: List[str] = None):
        self.__vcs = vcs
        self.__dictionaries = [] if dictionaries is None else dictionaries

    @property
    def vcs(self) -> str:
        return self.__vcs

    @vcs.setter
    def vcs(self, vcs: str):
        self.__vcs = vcs

    @property
    def dictionaries(self) -> List[str]:
        return self.__dictionaries

    @dictionaries.setter
    def dictionaries(self, dictionaries: List[str]):
        self.__dictionaries = dictionaries


class VcsConfigManager:
    def __init__(self):
        if not os.path.isfile(CONFIG_FILE):
            self.__config = VcsConfig()
        else:
            with open(CONFIG_FILE, 'r') as f:
                self.__config = json.load(f)

    @property
    def config(self) -> VcsConfig:
        return self.__config

    @config.setter
    def config(self, config: VcsConfig):
        self.__config = config
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f)


CONFIG_MANAGER = VcsConfigManager()
