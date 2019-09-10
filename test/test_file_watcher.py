import unittest
from unittest.mock import Mock, MagicMock

from plover_vcs.file_watcher import FileWatcher


class TestFileWatcher(unittest.TestCase):
    def setUp(self):
        self.mock_vcs = Mock()
        self.mock_message_gen = Mock()
        self.file_watcher = FileWatcher(lambda s: self.mock_vcs, self.mock_message_gen)
        self.file_watcher.watcher = Mock()

    def test_watch_file(self):
        self.file_watcher.watcher.addPath = Mock()
        self.file_watcher.watch_file('file-path')
        self.file_watcher.watcher.addPath.assert_called_with('file-path')

    def test_file_changed_handler(self):
        self.mock_vcs.diff = Mock(return_value='diff-value')
        self.mock_message_gen.get_message = Mock(return_value='commit-message')
        self.mock_vcs.commit = Mock()

        self.file_watcher.file_changed('file-path')
        self.mock_vcs.commit.assert_called_with('file-path', 'commit-message')
