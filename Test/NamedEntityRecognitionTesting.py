import unittest
import sys
import os
sys.path.append(os.path.join('..', 'Src'))
from NamedEntityRecognition import NamedEntityRecognition
from Tagging import PartOfSpeechTagging
from Tokenization import TextTokenization

class NERTestCase(unittest.TestCase):

	def testNER(self):
		sentence = "Yesterday Ivan Blake, Abdul Haseeb Hussain and Adam Allen Jones went to work for the summer after working at Google. Johnathon Allen, Mahatma Ghandi and Tom Smith are also planning to go tomorrow to Apple. Anna Rose and Fiona Smith."
		tokenization = TextTokenization()
		tokenizedSentence = tokenization.wordTokenize(sentence)
		tagging  = PartOfSpeechTagging()
		taggedSentence = tagging.customTagging(tokenizedSentence)
		ner = NamedEntityRecognition()
		entitiesRecognised = ner.namedEntityRecognition(taggedSentence[1])
		persons = []
		for subtree in entitiesRecognised.subtrees(filter=lambda t: t.label() == 'PERSON'):
			personName = []
			for leaf in subtree.leaves():
				personName.append(leaf[0])
			personName = " ".join(personName)
			persons.append(personName)
		expectedPersons = ['Ivan Blake', 'Abdul Haseeb Hussain', 'Adam Allen Jones', 'Johnathon Allen', 'Mahatma Ghandi', 'Tom Smith', 'Anna Rose', 'Fiona Smith']
		self.assertCountEqual(persons, expectedPersons)

if __name__ == '__main__':
	unittest.main()