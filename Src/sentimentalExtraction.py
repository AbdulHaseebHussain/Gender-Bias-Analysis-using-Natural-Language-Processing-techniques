import nltk
import nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews, stopwords



class SentimentExtraction():

	def wordFeatures(self, words):
		return dict([(word, True) for word in words])	 

	def extractSentimentSentence(self):

		positiveReviews = movie_reviews.fileids('pos')
		negativeReviews = movie_reviews.fileids('neg')

		negativeFeatures = [(self.wordFeatures(movie_reviews.words(fileids=[f])), 'negative') for f in negativeReviews]
		positiveFeatures = [(self.wordFeatures(movie_reviews.words(fileids=[f])), 'positive') for f in positiveReviews]

		negativeCutoff = int(len(negativeFeatures)*9/10)
		positiveCutoff = int(len(positiveFeatures)*9/10)

		print(negativeCutoff)
		print(positiveCutoff)

		trainingFeatures = positiveFeatures[:positiveCutoff]+negativeFeatures[:negativeCutoff]
		testFeatures = positiveFeatures[positiveCutoff:]+negativeFeatures[negativeCutoff:]
		print('Training on %d instances and Testing on %d instances' % (len(trainingFeatures), len(testFeatures)))

		classifier = NaiveBayesClassifier.train(trainingFeatures)
		print(classifier.classify(self.wordFeatures("He was feeling terrible though he later felt ecstatic")))
		#print(classifier.classify(self.wordFeatures("She was feeling terrible")))
		print('Accuracy:', nltk.classify.accuracy(classifier, testFeatures))

		print(classifier.show_most_informative_features())

if __name__ == '__main__':
	sentimentClass = SentimentExtraction()
	sentimentClass.extractSentimentSentence()

