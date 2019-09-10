import os
from typing import Callable

from PyQt5 import QtCore

from plover_vcs.message_generator.message_generator import MessageGenerator
from plover_vcs.vcs.vcs_service import VcsService


class FileWatcher:
    def __init__(self, vcs_factory: Callable[[str], VcsService], message_gen: MessageGenerator):
        """
        Creates a class that handles watching files and committing changes to them.
        :param vcs_factory: factory for creating VcsService
        :param message_gen: commit message generator
        """
        self.vcs_factory = vcs_factory
        self.message_gen = message_gen
        self.watcher = QtCore.QFileSystemWatcher()
        self.watcher.fileChanged.connect(self.file_changed)

    def watch_file(self, file: str):
        """
        Registers the given file to be watched and version controlled
        :param file: path to file
        :return: nothing
        """
        self.watcher.addPath(file)

    def file_changed(self, path):
        """
        Handler that commits the changes as soon as they are detected
        :param path: file to commit
        :return: nothing
        """
        vcs = self.vcs_factory(os.path.dirname(path))
        diff = vcs.diff(path)
        if diff:
            commit_message = self.message_gen.get_message(diff)
            vcs.commit(path, commit_message)
