import platform
import unittest

from corrections.calc import Calculatrice


class TestCBasic(unittest.TestCase):

    def test_system(self):
        os_name = platform.system().lower()
        self.assertEqual(os_name,"linux")

