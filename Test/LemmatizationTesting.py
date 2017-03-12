import unittest
import sys
import os
sys.path.append(os.path.join('..', 'Src'))
from Normalization import TextNormalization

class TextLemmatizationTestCase(unittest.TestCase):

	def testLemmatization(self):
		word = "Is"
		wordTag = "V"
		normalize = TextNormalization()
		lowercasedWord = normalize.convertToLowercase(word)
		wordnetTag = normalize.wordnetPos(wordTag)
		lemmatizedWord = normalize.lemmatization(lowercasedWord, wordnetTag)
		self.assertEqual(lemmatizedWord, "be")

if __name__ == '__main__':
	unittest.main()