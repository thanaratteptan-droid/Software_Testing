import unittest
from coe_number.cat_and_mouse import cat_and_mouse

class CatAndMouseTest(unittest.TestCase):
    
    # Test Case 1: จากตัวอย่างในสไลด์ (1 2 3 -> Cat B)
    def test_give_1_2_3_should_be_cat_b(self):
        x, y, z = 1, 2, 3
        result = cat_and_mouse(x, y, z)
        self.assertEqual(result, "Cat B")

    # Test Case 2: จากตัวอย่างในสไลด์ (1 3 2 -> Mouse C)
    def test_give_1_3_2_should_be_mouse_c(self):
        x, y, z = 1, 3, 2
        result = cat_and_mouse(x, y, z)
        self.assertEqual(result, "Mouse C")

    # Test Case 3: จากตัวอย่างในสไลด์ (1 5 4 -> Cat B)
    def test_give_1_5_4_should_be_cat_b(self):
        x, y, z = 1, 5, 4
        result = cat_and_mouse(x, y, z)
        self.assertEqual(result, "Cat B")
        
    # Test Case 4: แมว A อยู่ใกล้กว่าบ้าง (เช่น A อยู่ 5, B อยู่ 1, หนูอยู่ 4)
    def test_give_5_1_4_should_be_cat_a(self):
        x, y, z = 5, 1, 4
        result = cat_and_mouse(x, y, z)
        self.assertEqual(result, "Cat A")

    # Test Case 5: แมวทั้งสองตัวอยู่ที่จุดเดียวกันเป๊ะๆ
    def test_give_same_position_cats_should_be_mouse_c(self):
        x, y, z = 2, 2, 5
        result = cat_and_mouse(x, y, z)
        self.assertEqual(result, "Mouse C")

if __name__ == '__main__':
    unittest.main()