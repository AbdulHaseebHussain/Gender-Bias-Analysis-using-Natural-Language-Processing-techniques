import nltk

from nltk.corpus import names
import random

class GenderClassify:

	def genderFeatures(self, word):
		return {"last letter":word[-1]}

	def genderClasify(self):

		labeledNames = ([(name, "male") for name in names.words("male.txt")]+
			[(name, "female") for name in names.words("female.txt")])

		random.shuffle(labeledNames)

    # Process the names through feature extractor
		feature_sets = [(self.genderFeatures(n), gender) for (n, gender) in labeledNames]

    # Divide the feature sets into training and test sets
		train_set, test_set = feature_sets[100:], feature_sets[:100]

    # Train the naiveBayes classifier
		classifier = nltk.NaiveBayesClassifier.train(train_set)

    	# Test out the classifier with few samples outside of training set
		print(classifier.classify(self.genderFeatures("Adam")))
		#print(classifier.classify(self.genderFeatures("trinity")))

		#Test the accuracy of the classifier on the test data
		print(nltk.classify.accuracy(classifier, test_set))  # returns 0.78 for now

    # examine classifier to determine which feature is most effective for
    # distinguishing the name's gender
		print(classifier.show_most_informative_features(5))

if __name__ == '__main__':
	genderClass = GenderClassify()
	genderClass.genderClasify()