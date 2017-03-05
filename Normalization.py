import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

class TextNormalization:

	def stemming(self, word):
		stemmer = PorterStemmer()
		stemmedWord = stemmer.stem(word)
		return stemmedWord

	def convertToLowercase(self, word):
		return word.lower()

	def lemmatization(self, word, tag):
		lemmatizer = WordNetLemmatizer()
		lemmatizedWord = lemmatizer.lemmatize(word, tag)
		return lemmatizedWord

	def wordnetPos(self, tag):
	    if tag.startswith('J'):
        	return wordnet.ADJ
	    elif tag.startswith('V'):
        	return wordnet.VERB
	    elif tag.startswith('N'):
        	return wordnet.NOUN
	    elif tag.startswith('R'):
        	return wordnet.ADV
	    else:
        	return ''
