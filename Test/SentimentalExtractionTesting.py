import unittest
import sys
import os
sys.path.append(os.path.join('..', 'Src'))
from SentimentalExtraction import SentimentExtraction


class SentimentExtractionTestCase(unittest.TestCase):

	def testGeneralSentimentAccuracy(self):
		sentimentClass = SentimentExtraction()
		sentence = 'The prom was pretty good and worthwhile'
		sentiment = sentimentClass.extractSentimentSentence(sentence)
		self.assertTrue(sentiment[1]>0.65)

	def testStronglyPositiveSentiment(self):
		sentimentClass = SentimentExtraction()
		sentence = 'The prom was set in a beautiful venue with a marvellous stage'
		sentiment = sentimentClass.extractSentimentSentence(sentence)
		self.assertEqual(sentiment[0], 'positive')

	def testStronglyNegativeSentiment(self):
		sentimentClass = SentimentExtraction()
		sentence = 'The prom was set in a disastrous venue with a tacky stage'
		sentiment = sentimentClass.extractSentimentSentence(sentence)
		self.assertEqual(sentiment[0], 'negative')

	def testMildlyPositiveSentiment(self):
		sentimentClass = SentimentExtraction()
		sentence = 'The prom was great though it was slighly long'
		sentiment = sentimentClass.extractSentimentSentence(sentence)
		self.assertEqual(sentiment[0], 'positive')

	def testMildlyNegativeSentiment(self):
		sentimentClass = SentimentExtraction()
		sentence = 'The prom was terrible though finished quick'
		sentiment = sentimentClass.extractSentimentSentence(sentence)
		self.assertEqual(sentiment[0], 'negative')

if __name__ == '__main__':
	unittest.main()