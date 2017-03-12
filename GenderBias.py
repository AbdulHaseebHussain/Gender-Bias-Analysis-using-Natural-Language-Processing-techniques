import sys
import os
sys.path.append(os.path.join('..', 'Src'))
from Tagging import PartOfSpeechTagging
from NamedEntityRecognition import NamedEntityRecognition
from GenderClassification import GenderClassify
from SentimentalExtraction import SentimentExtraction
from Tokenization import TextTokenization
from collections import Counter



class GenderBiased:

	def initialization(self, sentences):

		tokenization = TextTokenization()
		tagging  = PartOfSpeechTagging()
		ner = NamedEntityRecognition()
		gc = GenderClassify()
		se = SentimentExtraction()


		taggedSentence = tagging.customTagging(tokenization.wordTokenize(sentences))
		entitiesRecognised = ner.namedEntityRecognition(taggedSentence[1])
		persons = []
		for subtree in entitiesRecognised.subtrees(filter=lambda t: t.label() == 'PERSON'):
			personName = []
			for leaf in subtree.leaves():
				personName.append(leaf[0])
			personName = " ".join(personName)
			persons.append(personName)
		return persons

	def getSentencesOfPerson(self, sentences, person):
		tokenization = TextTokenization()
		tokenizedSentences = tokenization.sentenceTokenize(sentences)
		personSentences = []
		for sentence in tokenizedSentences:
			if person in sentence:
				personSentences.append(sentence)
		return personSentences

	def getSentenceSentiment(self, sentences):
		se = SentimentExtraction()
		sentence = ' '.join(sentences)
		sentiment = se.extractSentimentSentence(sentence)[0]
		return sentiment

	def percentagesNegativePositive(self, genderSentiment):
		totalSentimentFrequency = Counter(genderSentiment)
		positiveFrequency = totalSentimentFrequency['positive']
		negativeFrequency = totalSentimentFrequency['negative']
		try:
			positivePercentage = (int)(positiveFrequency/(positiveFrequency+negativeFrequency) * 100)
		except ZeroDivisionError:
			positivePercentage = 0

		try:
			negativePercentage = (int)(negativeFrequency/(positiveFrequency+negativeFrequency) * 100)
		except ZeroDivisionError:
			negativePercentage = 0

		return [positivePercentage, negativePercentage]


	def assessBias(self, sentences):
		gc = GenderClassify()
		persons = self.initialization(sentences)

		maleSentiment = []
		femaleSentiment = []

		for person in persons:
			genderOfPerson = gc.genderClassify(person)[0]
			personSentences = self.getSentencesOfPerson(sentences, person)
			sentiment = self.getSentenceSentiment(personSentences)
			if genderOfPerson == 'male':
				maleSentiment.append(sentiment)
			else:
				femaleSentiment.append(sentiment)

		malePercentageSentiment = self.percentagesNegativePositive(maleSentiment)
		femalePercentageSentiment = self.percentagesNegativePositive(femaleSentiment)

		print('Male Sentiment Percentage')
		print('Male positive Sentiment : ', malePercentageSentiment[0], '%')
		print('Male negative Sentiment : ', malePercentageSentiment[1], '%\n')

		print('Female Sentiment Percentage')
		print('female positive Sentiment : ', femalePercentageSentiment[0], '%')
		print('female negative Sentiment : ', femalePercentageSentiment[1], '%')

		return [malePercentageSentiment, femalePercentageSentiment]



