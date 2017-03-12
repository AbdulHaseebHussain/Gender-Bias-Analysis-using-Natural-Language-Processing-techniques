import nltk
import nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews, stopwords
import pickle



class SentimentExtraction:

	def wordFeatures(self, words):
		return dict([(word, True) for word in words])	 

	def extractSentimentSentence(self, sentence):

		positiveReviews = movie_reviews.fileids('pos')
		negativeReviews = movie_reviews.fileids('neg')

		negativeFeatures = [(self.wordFeatures(movie_reviews.words(fileids=[f])), 'negative') for f in negativeReviews]
		positiveFeatures = [(self.wordFeatures(movie_reviews.words(fileids=[f])), 'positive') for f in positiveReviews]

		negativeCutoff = int(len(negativeFeatures)*0.75)
		positiveCutoff = int(len(positiveFeatures)*0.75)

		#trainingFeatures = positiveFeatures[:positiveCutoff]+negativeFeatures[:negativeCutoff]
		testFeatures = positiveFeatures[positiveCutoff:]+negativeFeatures[negativeCutoff:]
		#print('Training on %d instances and Testing on %d instances' % (len(trainingFeatures), len(testFeatures)))

		#classifier = NaiveBayesClassifier.train(trainingFeatures)
		#with open('../Src/Classifiers/dumpedSentimentalClassifier.pkl', 'wb') as sentimentalFile:
			#pickle.dump(classifier, sentimentalFile)
		with open('../Src/Classifiers/dumpedSentimentalClassifier.pkl', 'rb') as sentimentalFile:
			classifier = pickle.load(sentimentalFile)

		sentenceSentiment = classifier.classify(self.wordFeatures(sentence))
		#print(classifier.classify(self.wordFeatures("She was feeling terrible")))

		sentimentAccuracy = nltk.classify.accuracy(classifier, testFeatures)

		returned  = [sentenceSentiment, sentimentAccuracy]
		return returned
		#print(classifier.show_most_informative_features())

