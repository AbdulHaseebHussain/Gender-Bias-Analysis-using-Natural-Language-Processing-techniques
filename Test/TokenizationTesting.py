import unittest
import sys
import os
sys.path.append(os.path.join('..', 'Src'))
from Tokenization import TextTokenization

class TextTokenizationTestCase(unittest.TestCase):

	def testSentenceTokenization(self):
		rawText = "Hello World. How are you?"
		tokenization = TextTokenization()
		extractedSentences = tokenization.sentenceTokenize(rawText)
		expectedSentences = ['Hello World.', 'How are you?']
		self.assertCountEqual(extractedSentences, expectedSentences)

	def testWordTokenization(self):
		rawText = "Hello World's. How are' You today in Calledonian-Thistle! 12345"
		tokenization = TextTokenization()
		extractedWords  = tokenization.wordTokenize(rawText)
		expectedWords = ['Hello','World\'s', '.', 'How', 'are\'','You', 'today', 'in', 'Calledonian-Thistle', '!']
		self.assertCountEqual(extractedWords, expectedWords)

if __name__ == '__main__':
	unittest.main()
