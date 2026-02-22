import unittest
from unittest.mock import patch
from coe_number.random_utils import guess_int, guess_float

class RandomUtilsTest(unittest.TestCase):

    # ใช้ @patch เพื่อจำลองฟังก์ชัน random.randint
    @patch('coe_number.random_utils.random.randint')
    def test_guess_int_should_return_mocked_value(self, mock_randint):
        # Arrange: ล็อกผลลัพธ์ให้ random.randint ตอบ 5 เสมอ
        mock_randint.return_value = 5
        
        # Act: เรียกใช้ฟังก์ชันที่อยู่ในโค้ดหลักของเรา
        result = guess_int(1, 10)
        
        # Assert: เช็กว่าได้ 5 ตามที่เราล็อกผลไว้หรือไม่
        self.assertEqual(result, 5)
        
        # เช็กเสริม: ตรวจสอบว่าฟังก์ชัน randint ถูกเรียกใช้งานด้วยพารามิเตอร์ (1, 10) จริงๆ
        mock_randint.assert_called_with(1, 10)


    # ใช้ @patch เพื่อจำลองฟังก์ชัน random.uniform
    @patch('coe_number.random_utils.random.uniform')
    def test_guess_float_should_return_mocked_value(self, mock_uniform):
        # Arrange: ล็อกผลลัพธ์ให้เป็น 7.5
        mock_uniform.return_value = 7.5
        
        # Act
        result = guess_float(1.0, 10.0)
        
        # Assert
        self.assertEqual(result, 7.5)
        mock_uniform.assert_called_with(1.0, 10.0)


