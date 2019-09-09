import unittest

from plover_vcs.message_generator.git_diff_message_generator import GitSingleFileDiffMessageGenerator, file_name
from plover_vcs.message_generator.line_changes import LineChanges

diff = """diff --git a/dictionary/main.json b/dictionary/main.json
index e1c35fb..c285bbc 100755
--- a/dictionary/main.json
+++ b/dictionary/main.json
@@ -1,3 +1,11 @@
 {
-"PHREU": "apply"
+"AFPS": "{*?}",
+"HRO*ERD": "{^}{*>}",
+"KA*PS": "{MODE:CAPS}",
+"KHEBGT": "checkout",
+"PHR-R": "{MODE:RESET}",
+"PHREU": "apply",
+"STPH": "{^}https://{^}",
+"STPH*": "{^}http://{^}",
+"TK-FPS": "{*!}"
 }
"""

expected_commit_message = """Update main.json

Added Stroke: AFPS → {*?}
Added Stroke: HRO*ERD → {^}{*>}
Added Stroke: KA*PS → {MODE:CAPS}
Added Stroke: KHEBGT → checkout
Added Stroke: PHR-R → {MODE:RESET}
Added Stroke: PHREU → apply
Added Stroke: STPH → {^}https://{^}
Added Stroke: STPH* → {^}http://{^}
Added Stroke: TK-FPS → {*!}
Deleted Stroke: PHREU → apply"""


class TestGitSingleFileDiffMessageGenerator(unittest.TestCase):
    def setUp(self):
        self.message_generator = GitSingleFileDiffMessageGenerator()

    def test_get_filename(self):
        filename = self.message_generator.get_filename(diff)
        self.assertEqual('main.json', filename)

    def test_get_filename_no_match(self):
        print()
        filename = self.message_generator.get_filename('index e1c35fb..c285bbc 100755')
        self.assertEqual(None, filename)

    def test_get_line_changes(self):
        line_changes = self.message_generator.get_line_changes(diff)
        self.assertListEqual([
            '"AFPS": "{*?}",',
            '"HRO*ERD": "{^}{*>}",',
            '"KA*PS": "{MODE:CAPS}",',
            '"KHEBGT": "checkout",',
            '"PHR-R": "{MODE:RESET}",',
            '"PHREU": "apply",',
            '"STPH": "{^}https://{^}",',
            '"STPH*": "{^}http://{^}",',
            '"TK-FPS": "{*!}"'
        ], line_changes.added)
        self.assertListEqual(['"PHREU": "apply"'], line_changes.deleted)

    def test_format_dictionary_change_no_key_value_pair(self):
        result = self.message_generator.format_dictionary_change('Non Key-value pair line')
        self.assertIsNone(result)

    def test_format_dictionary_change(self):
        result = self.message_generator.format_dictionary_change('"HRO*ERD": "{^}{*>}"')
        self.assertEqual('HRO*ERD → {^}{*>}', result)

    def test_format_lines_prefix(self):
        result = self.message_generator.format_lines(['"A": "B"', '"C": "D"'], 'prefix ')
        self.assertEqual('prefix A → B\nprefix C → D', result)

    def test_format_lines_filters_none_entries(self):
        result = self.message_generator.format_lines(['INVALID', '"C": "D"'])
        self.assertEqual('C → D', result)

    def test_format_commit_body(self):
        line_changes = LineChanges()
        line_changes.added = ['"A": "B"']
        line_changes.deleted = ['"C": "D"']
        result = self.message_generator.format_commit_body(line_changes)
        self.assertEqual('Added Stroke: A → B\nDeleted Stroke: C → D', result)

    def test_get_message(self):
        message = self.message_generator.get_message(diff)
        self.assertEqual(expected_commit_message, message)
