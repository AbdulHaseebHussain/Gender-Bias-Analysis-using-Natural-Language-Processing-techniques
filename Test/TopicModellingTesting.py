import unittest
import sys
import os
sys.path.append(os.path.join('..', 'Src'))
from topicModelling import TopicModelling

class TopicModellingTestCase(unittest.TestCase):

	def testTopicModelling(self):
		documents = ['Human machine interface for lab abc computer applications',\
             'A survey of user opinion of computer system response time',\
             'The EPS user interface management system',\
             'System and human system engineering testing of EPS',\
             'Relation of user perceived response time to error measurement',\
             'The generation of random binary unordered trees',\
             'The intersection graph of paths in trees',\
             'Graph minors IV Widths of trees and well quasi ordering',\
             'Graph minors A survey']


		modelling = TopicModelling()
		modelling.topicModelling(documents)

		self.assertTrue(True)


if __name__ == '__main__':
	unittest.main()