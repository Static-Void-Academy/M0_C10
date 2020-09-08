from sys import platform
import unittest

from pexpect import replwrap

class TestLibraryCatalog(unittest.TestCase):
    def assert_interactions(self, tests):
        for interaction in tests:
            output = self.child.run_command(interaction[0])
            self.assertEqual(interaction[1], output)

    def setUp(self):
        command = 'python'
        if platform == 'linux' or platform == 'darwin':
            command += '3'
        self.child = replwrap.REPLWrapper(f'{command} library_catalog.py', '? ', None)

    def test_simple(self):
        """Tests show"""
        tests = [('Show','  John Steinbeck:\n    The Grapes of Wrath: 5\n    Of Mice and Men: 3\n  Sun Tzu:\n    The Art of War: 3\n  Stephanie Meyer:\n    Twilight: 2\n    Breaking Dawn: 1\n  Gayle Laakmann McDowell:\n    Cracking the Coding Interview: 4\n    Cracking the PM Interview: 3\n  Dan Brown:\n    The Da Vinci Code: 4\r\n')]
        self.assert_interactions(tests)

if __name__ == '__main__':
    unittest.main()
