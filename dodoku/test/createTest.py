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
        
    def test_Create_030_LowLevelValue(self):
        gridValue= [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,
                          -1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,
                          -2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,
                          0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,
                          -6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,
                          -5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
        hashValue = '5a3f0c31993d46bcb2ab5f3e8318e734231ee8bdb26cba545fadd7b1732888cd'
        statusValue = 'ok'
        parms = {'op':'create', 'level':'1'}
        result = create._create(parms)
        self.assertEqual(result.get('grid'), gridValue)
        self.assertIn(result.get('integrity'), hashValue)
        self.assertEqual(result.get('status'), statusValue)
        
    def test_Create_040_Integrityis8Digits(self):
        parms = {'op':'create','level':'1'}
        result = create._create(parms)
        self.assertEqual(len(result['integrity']),8)
        
    def test_Create_050_MaxLevelValue(self):
        gridValue= [0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,
                    -7,0,-8,-9,0,-9,0,0,-5,0,-2,0,0,-4,0,-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,0,0,
                    -3,0,0,0,0,0,0,0,-6,0,-4,0,0,0,-8,0,-7,0,0,0,0,0,0,0,-5,0,0,0,0,-1,0,-6,-3,0,0,0,
                    -9,-8,0,-5,0,-1,-2,0,-2,0,0,-7,0,-1,0,0,-3,0,-4,-3,0,-8,0,-6,-5,0,0,0,-7,-3,0,-5,
                    -9,0,0,0,0,0,-4,0,-2,0,0,0,0,0,0,0,-6,0,0,0,0] 
        hashValue = 'eb572835ffe2015c731057f94d46fa77430ad6fd332abb0d7dd39d5f2ccadea9'
        statusValue = 'ok'
        parms = {'op':'create', 'level':'3'}
        result = create._create(parms)
        self.assertEqual(result.get('grid'), gridValue)
        self.assertIn(result.get('integrity'), hashValue)
        self.assertEqual(result.get('status'), statusValue)
        