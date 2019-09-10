from abc import ABC, abstractmethod

from plover_vcs.vcs.git_vcs_service import GitVcsService
from plover_vcs.vcs_config import CONFIG_MANAGER


class VcsService(ABC):
    def __init__(self, repo: str):
        """
        Creates the VcsService
        :param repo: repo path
        """

    @abstractmethod
    def commit(self, file: str, message: str):
        """
        Commits the given file to the underlying repo with the given message
        :param file: file to commit
        :param message: commit message
        """

    @abstractmethod
    def diff(self, file: str):
        """
        Commits the given file.
        :param file: file to commit
        :return:
        """


class VcsException(Exception):
    """
    Exception for errors thrown by VcsService
    """


IMPLEMENTATIONS = {
    'git': GitVcsService
}


def vcs_service_factory(repo: str):
    return IMPLEMENTATIONS[CONFIG_MANAGER.config](repo)
