import unittest
import sys
import os
sys.path.append(os.path.join('..', 'Src'))
from Tagging import PartOfSpeechTagging
from Tokenization import TextTokenization

class TextTaggingTestCase(unittest.TestCase):

	def testTagging(self):
		sents = "Tom thinks John is terrible. John thinks Tom is great."
		speechTagging = PartOfSpeechTagging()
		tokenization = TextTokenization()
		trainedTag = (speechTagging.customTagging(tokenization.wordTokenize(sents)))
		trainedTagEvaluation = trainedTag[0]
		expectedTagging = [('Tom', 'NNP'), ('thinks', 'VBZ'), ('John', 'NNP'), ('is', 'VBZ'), ('terrible', 'JJ'), ('.', '.'), ('John', 'NNP'), ('thinks', 'VBZ'), ('Tom', 'NNP'), ('is', 'VBZ'), ('great', 'JJ'), ('.', '.')]
		print("Accuracy with Treebank corpus: ",trainedTagEvaluation*100)
		print(trainedTag[1])
		self.assertTrue((expectedTagging==trainedTag[1]) and (trainedTagEvaluation>0.90))

if __name__ == '__main__':
	unittest.main()	