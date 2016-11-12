import unittest
import sys
import os
sys.path.append(os.path.join('..', 'Src'))
from Tagging import PartOfSpeechTagging
from nltk.corpus import brown

##UNIT TESTS ARE AUTOMATICALLY REGRESSION TESTS

class TextTaggingTestCase(unittest.TestCase):

	def testTagging(self):
		brown_sents = brown.sents(categories='news')
		speechTagging = PartOfSpeechTagging()
		trainedTagEvaluation = speechTagging.partOfSpeechTagging(brown_sents[2007])
		self.assertTrue(trainedTagEvaluation>0.5)

if __name__ == '__main__':
	unittest.main()