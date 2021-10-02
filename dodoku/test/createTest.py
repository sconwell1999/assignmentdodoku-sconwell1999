from unittest import TestCase
import dodoku.create as create 

class CreateTest(TestCase):
    def test_Create_010_ShouldReturn3Keys(self):
        expectedResult = {'grid':'', 'integrity':'', 'status':''}
        parms = {'op':'create','level':'1'}
        actualResult = create._create(parms)
        self.assertEqual(expectedResult.keys(), actualResult.keys())
        
    def test_Create_020_NominalLevelValue(self):
        gridValue= [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,
                       0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,
                       0,0,0,0,0,0,0,0,-7,0,0,0,0,0,0,0,0,-5,0,-8,0,-4,0,0,-1,0,0,
                       0,-7,0,0,-6,0,-2,0,-9,0,0,0,0,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,
                       -9,-5,-3,0,0,-7,0,-4,0,0,0,0,0,-5,-8,0,0,-1,0,0,-9,0,0,0
                       ,-2,-1,0,0,0,0,0,0,0,0,0,-9,-8,0,-6,-1,-6,-1,0,0,0,0,0,-7,0]
        hashValue = '6fcd71ef7722e7573d2f607a35cfa48f72b03c4cea135ac31f7ef73a58e50a8a'
        statusValue = 'ok'
        parms = {'op':'create', 'level':'2'}
        result = create._create(parms)
        self.assertEqual(result.get('grid'), gridValue)
        self.assertIn(result.get('integrity'), hashValue)
        self.assertEqual(result.get('status'), statusValue)
        