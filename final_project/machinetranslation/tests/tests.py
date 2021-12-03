
import unittest
from .. import translator

class TranslationTests(unittest.TestCase):

    def test_frenchToEnglish_null(self):
        self.assertNotEqual( translator.frenchToEnglish(), "Hello")

    def test_englishToFrench_null(self):
        self.assertNotEqual( translator.englishToFrench(), "Bonjour")

    def test_frenchToEnglish_hello(self):
        self.assertEqual( translator.frenchToEnglish("Bonjour"), "Hello")

    def test_englishToFrench_hello(self):
        self.assertEqual( translator.englishToFrench("Hello"), "Bonjour")

if __name__ == "__main__":
    unittest.main()