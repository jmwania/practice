import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
       
        self.assertEqual(calc.add(10, 6 ), 16)
        self.assertEqual(calc.add(100, 6 ), 106)
        self.assertEqual(calc.add(120, 7 ), 127)
        self.assertEqual(calc.add(1000, 6 ), 1006)

    def test_subtract(self):
       
        self.assertEqual(calc.subtract(10, 6 ), 4)
        self.assertEqual(calc.subtract(100, 6 ), 94)
        self.assertEqual(calc.subtract(30, 9 ), 21)
    
    def test_multily(self):
       
        self.assertEqual(calc.multiply(10, 6 ), 60)
        self.assertEqual(calc.multiply(100, 6 ), 600)
        self.assertEqual(calc.multiply(30, 9 ), 270)
        
    
    def test_divide(self):
       
        self.assertEqual(calc.divide(10, 5 ), 2)
        self.assertEqual(calc.divide(100, 20 ), 5)
        self.assertEqual(calc.divide(10, 2 ), 5)
        
        # Raises ValueError
        self.assertRaises(ValueError, calc.divide, 10, 0)

        
        # Alternatively, Raises ValueError using cotext manager
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ =='__main__':
    unittest.main()