import unittest
import sys
import os
sys.path.append(os.path.join('..', 'Src'))
from GenderBias import GenderBiased

class GenderBiasTestCase(unittest.TestCase):

	def testPositiveMaleBias(self):
		sentences = 'It is said Thomas Jones was a man of upstanding character and grace. It is said Anna Smith was a women of terrible character.'
		gb = GenderBiased()
		malePercentageSentiment = gb.assessBias(sentences)[0]
		self.assertTrue(malePercentageSentiment[0]==100)

	def testNegativeMaleBias(self):
		sentences = 'It is said Thomas Jones was a man of upstanding character and grace. It is said Anna Smith was a women of terrible character.'
		gb = GenderBiased()
		malePercentageSentiment = gb.assessBias(sentences)[0]
		self.assertTrue(malePercentageSentiment[1]==0)

	def testPositiveFemaleBias(self):
		sentences = 'It is said Thomas Jones was a man of upstanding character and grace. It is said Anna Smith was a women of terrible character.'
		gb = GenderBiased()
		femalePercentageSentiment = gb.assessBias(sentences)[1]
		self.assertTrue(femalePercentageSentiment[0]==0)

	def testNegativeFemaleBias(self):
		sentences = 'It is said Thomas Jones was a man of upstanding character and grace. It is said Anna Smith was a women of terrible character.'
		gb = GenderBiased()
		femalePercentageSentiment = gb.assessBias(sentences)[1]
		self.assertTrue(femalePercentageSentiment[1]==100)



if __name__ == '__main__':
	unittest.main()