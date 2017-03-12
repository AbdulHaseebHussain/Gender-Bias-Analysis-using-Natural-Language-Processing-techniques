import nltk
from nltk import AffixTagger, UnigramTagger, BigramTagger, DefaultTagger, TrigramTagger
from nltk.tag.perceptron import PerceptronTagger
from nltk.corpus import brown, conll2000, treebank
from  nltk.tag.brill import *
import nltk.tag.brill as brill
import nltk.tag.brill_trainer as bt
from nltk.tbl.template import Template 
import pickle


class PartOfSpeechTagging:

	def customTagging(self, dataToTag):

		trainingTestSplit = int(len(treebank.tagged_sents())*0.8)

		#trainingData = treebank.tagged_sents()[:trainingTestSplit]
		testData = treebank.tagged_sents()[trainingTestSplit:]

		#defaultTagger = DefaultTagger('NN')
		#affixTagger = AffixTagger(trainingData, affix_length=-2, min_stem_length=3, backoff=defaultTagger)
		#unigramTagger = UnigramTagger(trainingData, backoff=affixTagger)
		#bigramTagger = BigramTagger(trainingData, backoff=unigramTagger)
		#trigramTagger = TrigramTagger(trainingData, backoff=bigramTagger)

		#Template._cleartemplates()
		#templates = fntbl37()

		#brillTagger = bt.BrillTaggerTrainer(trigramTagger, templates, trace=3)
		#brillTagger = brillTagger.train(trainingData, max_rules=250)

		#with open('../Src/Taggers/brillTagger.pkl', 'wb') as taggingFile:
			#pickle.dump(brillTagger, taggingFile)

		with open('../Src/Taggers/brillTagger.pkl', 'rb') as taggingFile:
			brillTagger = pickle.load(taggingFile)		

		evaluation = brillTagger.evaluate(testData)
		tagData = brillTagger.tag(dataToTag)
		evalTag = [evaluation, tagData]
		return evalTag