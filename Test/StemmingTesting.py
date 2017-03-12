import unittest
import sys
import os
sys.path.append(os.path.join('..', 'Src'))
from Normalization import TextNormalization

class TextStemmingTestCase(unittest.TestCase):

	def testStemming(self):
		words = ["Walking", "Walks", "walked", "walk"]
		stemsFound = set()
		normalize = TextNormalization()
		for word in words:	
			stemmedWord = normalize.stemming(word)
			stemsFound.add(stemmedWord)
		self.assertTrue(("walk" in stemsFound) and (len(stemsFound)==1))

if __name__ == '__main__':
	unittest.main()