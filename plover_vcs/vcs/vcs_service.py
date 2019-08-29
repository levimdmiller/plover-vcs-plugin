from abc import ABC, abstractmethod


class VcsService(ABC):
    @abstractmethod
    def add(self, file: str):
        """
        Adds the given file to the files to be committed.
        :param file:
        """

    @abstractmethod
    def commit(self, message: str):
        """
        Commits the given file to the underlying repo with the given message
        :param message: commit message
        """

    @abstractmethod
    def pull(self):
        """
        Pulls the most recent changes.
        """

    @abstractmethod
    def switch(self, branch: str):
        """
        Switches to the given branch
        :param branch: name of branch
        """


class VcsException(Exception):
    """
    Exception for errors thrown by VcsService
    """
