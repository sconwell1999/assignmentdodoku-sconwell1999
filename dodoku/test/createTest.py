from unittest import TestCase
import dodoku.create as create 

class CreateTest(TestCase):
    def test_Create_010_ShouldReturn3Keys(self):
        expectedResult = {'grid':'', 'integrity':'', 'status':''}
        parms = {'op':'create','level':'1'}
        actualResult = create._create(parms)
        self.assertEqual(expectedResult.keys(), actualResult.keys())