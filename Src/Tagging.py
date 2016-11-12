import nltk
from nltk.tag import pos_tag
from nltk import FreqDist
from nltk import ConditionalFreqDist
from nltk import UnigramTagger, BigramTagger, DefaultTagger, TrigramTagger
from nltk.corpus import brown
from  nltk.tag.brill import *
import nltk.tag.brill_trainer as bt
from nltk.tbl.template import Template 

		
class PartOfSpeechTagging:

	def partOfSpeechTagging(self, rawText):
		brownTaggedSents = brown.tagged_sents(categories='news')
		defaultTagger = DefaultTagger('NN')
		affixTagger = nltk.AffixTagger(brownTaggedSents, affix_length=-2, min_stem_length=3, backoff=defaultTagger)
		unigramTagger = UnigramTagger(brownTaggedSents, backoff=affixTagger)
		bigramTagger = BigramTagger(brownTaggedSents, backoff=unigramTagger)
		trigramTagger = TrigramTagger(brownTaggedSents, backoff=bigramTagger)

		Template._cleartemplates()
		templates = fntbl37()
		brillTagger = bt.BrillTaggerTrainer(trigramTagger, templates, trace=3)
		brillTagger = brillTagger.train(brownTaggedSents, max_rules=250)
		evaluation = brillTagger.evaluate(brownTaggedSents)
		print(evaluation)
		return evaluation