import json
import os
from typing import List
from plover.config import CONFIG_DIR


# Config path.
CONFIG_FILE = os.path.join(CONFIG_DIR, 'plover_vcs.json')


class VcsConfig:
    def __init__(self, vcs: str = "", dictionaries: List[str] = None):
        self.vcs = vcs
        self.dictionaries = [] if dictionaries is None else dictionaries

    def fromJson(json):
        return VcsConfig(vcs = json.get("vcs", ""), dictionaries = json.get("dictionaries", []))

class VcsConfigManager:
    def __init__(self):
        if not os.path.isfile(CONFIG_FILE):
            self.config = VcsConfig()
        else:
            with open(CONFIG_FILE, 'r') as f:
                self.__config = VcsConfig.fromJson(json.load(f))

    @property
    def config(self) -> VcsConfig:
        return self.__config

    @config.setter
    def config(self, config: VcsConfig):
        self.__config = config
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config.__dict__, f)


CONFIG_MANAGER = VcsConfigManager()
