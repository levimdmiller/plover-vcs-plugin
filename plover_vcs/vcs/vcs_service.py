from abc import ABC, abstractmethod


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
    def diff(self, file: str) -> str:
        """
        Commits the given file.
        :param file: file to commit
        :return:
        """
