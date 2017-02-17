import unittest
import sys
import os
sys.path.append(os.path.join('..', 'Src'))
from Tagging import PartOfSpeechTagging
from nltk.corpus import brown
from nltk.tokenize import sent_tokenize, word_tokenize

##UNIT TESTS ARE AUTOMATICALLY REGRESSION TESTS

class TextTaggingTestCase(unittest.TestCase):

	def testTagging(self):
		brown_sents = "Adam thinks John is terrible. John thinks Adam is great"
		speechTagging = PartOfSpeechTagging()
		trainedTag = (speechTagging.customTagging(word_tokenize(brown_sents)))
		trainedTagEvaluation = trainedTag[0]
		print(trainedTag[1])
		self.assertTrue(trainedTagEvaluation>0.5)

if __name__ == '__main__':
	unittest.main()