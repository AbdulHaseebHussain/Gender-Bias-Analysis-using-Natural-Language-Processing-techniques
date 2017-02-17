import nltk
from nltk.tag import pos_tag
from nltk import FreqDist
from nltk import ConditionalFreqDist
from nltk import AffixTagger, UnigramTagger, BigramTagger, DefaultTagger, TrigramTagger
from nltk.tag.perceptron import PerceptronTagger
from nltk.corpus import brown, conll2000, treebank
from  nltk.tag.brill import *
import nltk.tag.brill as brill
import nltk.tag.brill_trainer as bt
from nltk.tbl.template import Template 
from nltk.tokenize import sent_tokenize, word_tokenize


class PartOfSpeechTagging:

	def customTagging(self, dataToTag):

		trainingData = treebank.tagged_sents()
		testData = brown.tagged_sents()
		defaultTagger = DefaultTagger('NN')
		#perceptionTagger = PerceptronTagger()
		affixTagger = nltk.AffixTagger(trainingData, affix_length=-2, min_stem_length=3, backoff=defaultTagger)
		unigramTagger = UnigramTagger(trainingData, backoff=affixTagger)
		bigramTagger = BigramTagger(trainingData, backoff=unigramTagger)
		trigramTagger = TrigramTagger(trainingData, backoff=bigramTagger)

		Template._cleartemplates()
		templates = fntbl37()

		brillTagger = bt.BrillTaggerTrainer(trigramTagger, templates, trace=3)
		brillTagger = brillTagger.train(trainingData, max_rules=250)
		evaluation = brillTagger.evaluate(testData)
		tagData = brillTagger.tag(dataToTag)
		print(evaluation)
		evalTag = [evaluation, tagData]
		return evalTag

	def standardTagging(self, dataToTag):
		return pos_tag(dataToTag)