from typing import List, Optional

from plover_vcs.message_generator.line_changes import LineChanges
from plover_vcs.message_generator.message_generator import MessageGenerator
import re

# matches a line like:  @@ -1,3 +1,11 @@
changes_start = re.compile('@@[^@]*@@')

# matches a line like: "PHREU": "apply",
dictionary_line = re.compile('"(.*)": ?"(.*)",?')

# matches:  diff --git a/path/to/file/file.json
file_name = re.compile('diff --git .*\/([^\/\s]*)')


class GitSingleFileDiffMessageGenerator(MessageGenerator):
    """
    Formats a diff of a single file in the following format:
    diff --git a/path/to/file/file.json
    index e1c35fb..c285bbc 100755
    --- a/path/to/file/main.json
    +++ b/path/to/file/main.json
    @@ -1,3 +1,11 @@
    + addition
    - deletion
    """

    def get_message(self, diff: str) -> str:
        file_changed = self.get_filename(diff)
        line_changes = self.get_line_changes(diff)
        return "Update {}\n\n{}".format(file_changed, self.format_commit_body(line_changes))

    @staticmethod
    def get_filename(diff: str) -> Optional[str]:
        match = file_name.match(diff)
        if not match:
            return None
        return match.group(1)

    @staticmethod
    def get_line_changes(diff: str) -> LineChanges:
        file_changes = changes_start.split(diff)[1]
        lines = file_changes.splitlines()
        line_changes = LineChanges()
        line_changes.added = [
            add[1:] for add in lines if add.startswith('+')
        ]
        line_changes.deleted = [
            delete[1:] for delete in lines if delete.startswith('-')
        ]
        return line_changes

    @staticmethod
    def format_dictionary_change(line: str) -> Optional[str]:
        """
        If the line is a change to a json dictionary, format it as
        key: value
        :param line: line to format
        :return: formatted line
        """
        match = dictionary_line.match(line)
        if not match:
            return None
        return "{} → {}".format(*match.groups())

    def format_lines(self, lines: List[str], prefix: str = '') -> str:
        """
        formats the given lines:
        [1, 2] ->
        prefix1
        prefix2
        :param lines: lines to format together
        :param prefix: prefix to append to each line
        :return: lines as formatted string
        """
        formatted_lines = (self.format_dictionary_change(line) for line in lines)
        return '\n'.join(
            prefix + line
            for line in formatted_lines
            if line is not None
        )

    def format_commit_body(self, line_changes: LineChanges) -> str:
        body = self.format_lines(line_changes.added, 'Added Stroke: ')
        return body + '\n' + self.format_lines(line_changes.deleted, 'Deleted Stroke: ')
