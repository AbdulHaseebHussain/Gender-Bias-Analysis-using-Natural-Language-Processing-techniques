import nltk

from nltk.corpus import names
import random
import pickle

class GenderClassify:

	def genderFeatures(self, word):
		return {"last letter":word[-1]}

	def genderClassify(self, nameToFindGender):

		labeledNames = ([(name, "male") for name in names.words("male.txt")]+
			[(name, "female") for name in names.words("female.txt")])

		random.shuffle(labeledNames)

    # Process the names through feature extractor
		feature_sets = [(self.genderFeatures(n), gender) for (n, gender) in labeledNames]
		split = int(len(labeledNames)*0.75)
    # Divide the feature sets into training and test sets
		train_set, test_set = feature_sets[:split], feature_sets[split:]

    # Train the naiveBayes classifier
		#classifier = nltk.NaiveBayesClassifier.train(train_set)
		#with open('../Src/Classifiers/dumpedGenderClassifier.pkl', 'wb') as genderFile:
			#pickle.dump(classifier, genderFile)
		with open('../Src/Classifiers/dumpedGenderClassifier.pkl', 'rb') as genderFile:
			classifier = pickle.load(genderFile)
			



    	# Test out the classifier with few samples outside of training set
		gender = classifier.classify(self.genderFeatures(nameToFindGender))
		#print(classifier.classify(self.genderFeatures("trinity")))

		#Test the accuracy of the classifier on the test data
		accuracy = nltk.classify.accuracy(classifier, test_set) # returns 0.78 for now

    # examine classifier to determine which feature is most effective for
    # distinguishing the name's gender
		#print(classifier.show_most_informative_features(5))

		returned = [gender, accuracy]
		return returned