import nltk
from nltk import ne_chunk

class NamedEntityRecognition:

	def namedEntityRecognition(self, tagged):
		chunks = ne_chunk(tagged)
		return chunks