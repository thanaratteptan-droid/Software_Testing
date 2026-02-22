import unittest
from coe_number.staircase import staircase

class StaircaseTest(unittest.TestCase):
    
    # Test Case 1: สร้างบันไดขนาด 2 (จากตัวอย่างสไลด์อาจารย์)
    def test_give_2_with_hash_should_be_hh(self):
        # arrange
        n = 2
        pattern = '#'
        expected_output = \
        " #\n" + \
        "##"
        
        # act
        result = staircase(n, pattern)
        
        # assert
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    # Test Case 2: สร้างบันไดขนาด 4 (ค่าปกติ)
    def test_give_4_with_hash(self):
        # arrange
        n = 4
        pattern = '#'
        expected_output = \
        "   #\n" + \
        "  ##\n" + \
        " ###\n" + \
        "####"
        # act
        result = staircase(n, pattern)
        # assert
        self.assertEqual(result, expected_output)
        
    # Test Case 3: ทดสอบขอบเขตล่าง n = 1
    def test_give_1_should_be_one_hash(self):
        n = 1
        expected_output = "#"
        result = staircase(n)
        self.assertEqual(result, expected_output)

    # Test Case 4: ทดสอบเมื่อ n เกิน 30 
    def test_give_31_should_return_empty(self):
        n = 31
        expected_output = ""
        result = staircase(n)
        self.assertEqual(result, expected_output)

    # Test Case 5: ทดสอบเมื่อ n เป็นเลขติดลบ หรือ 0
    def test_give_negative_should_return_empty(self):
        n = -5
        expected_output = ""
        result = staircase(n)
        self.assertEqual(result, expected_output)

