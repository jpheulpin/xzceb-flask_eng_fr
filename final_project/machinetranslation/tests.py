import unittest
import translator

class TestEnglishToFrench(unittest.TestCase):
    def runTest(self):
        self.assertEqual(translator.english_to_french("Car"), "Voiture")
        self.assertEqual(translator.english_to_french(None), "")
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    def runTest(self):
        self.assertEqual(translator.french_to_english("Voiture"), "Car")
        self.assertEqual(translator.french_to_english(None), "")
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")

unittest.main()
