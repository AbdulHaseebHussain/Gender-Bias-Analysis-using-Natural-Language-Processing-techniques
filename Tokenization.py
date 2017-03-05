import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tokenize import WhitespaceTokenizer, RegexpTokenizer
from nltk.corpus import stopwords
import string

class TextTokenization:

	#sentence tokenization
	def sentenceTokenize(self, rawText):
		return sent_tokenize(rawText)

	#word tokenization
	def wordTokenize(self, sentence):
		sentence.lower()
		tokenizer = RegexpTokenizer(r"'?([a-zA-z'-]+)'?")
		tokens = tokenizer.tokenize(sentence)
		filteredWords = [w for w in tokens if not w in stopwords.words('english')]
		return filteredWords
