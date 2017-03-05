import logging
from gensim import corpora, models, similarities

class TopicModelling:

	def topicModelling(self, documents):
		documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

             dictionary = corpora.Dictionary(documents)

             corpus = [dictionary.doc2bow(document) for document in documents]
             corpora.WikiCorpus.serialize