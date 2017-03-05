import unittest
import sys
import os
sys.path.append(os.path.join('..', 'Src'))
from GenderClassification import GenderClassify

class GenderClassificationTestCase(unittest.TestCase):

	def testGeneralGenderAccuracy(self):
		genderClassification = GenderClassify()
		genderAccuracy = genderClassification.genderClassify('Adam')[1]
		print(genderAccuracy)
		self.assertTrue(genderAccuracy>0.65)



	def testFemale(self):
		genderClassification = GenderClassify()
		firstFemale = genderClassification.genderClassify("Anna")
		secondFemale = genderClassification.genderClassify("Katrina")
		thirdFemale = genderClassification.genderClassify("Sabrina")
		fourthFemale = genderClassification.genderClassify("Samantha")
		females = [firstFemale[0], secondFemale[0], thirdFemale[0], fourthFemale[0]]
		self.assertCountEqual(females, ['female', 'female', 'female', 'female'])

	def testMale(self):

		genderClassification = GenderClassify()
		firstMale = genderClassification.genderClassify("Abdul")
		secondMale = genderClassification.genderClassify("Apostolos")
		thirdMale = genderClassification.genderClassify("John")
		fourthMale = genderClassification.genderClassify("Thomas")
		males = [firstMale[0], secondMale[0], thirdMale[0], fourthMale[0]]
		self.assertCountEqual(males, ['male', 'male', 'male', 'male'])

if __name__ == '__main__':
	unittest.main()