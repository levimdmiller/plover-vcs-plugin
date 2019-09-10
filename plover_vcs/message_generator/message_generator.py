from abc import ABC, abstractmethod


class MessageGenerator(ABC):
    @abstractmethod
    def get_message(self, diff: str) -> str:
        """
        Generates a commit message from the given diff string
        :param diff: diff of the file to commit
        """
