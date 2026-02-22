import unittest
from coe_number.grid_challenge import gridChallenge

class GridChallengeTest(unittest.TestCase):
    def test_give_normal_grid_should_be_YES(self):
        # Arrange
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        # Act
        result = gridChallenge(grid)
        # Assert
        self.assertEqual(result, "YES")

    def test_give_unsorted_columns_should_be_NO(self):
        self.assertEqual(gridChallenge(['mpxz', 'abcd', 'wlmf']), "NO")

    def test_give_single_row_should_be_YES(self):
        self.assertEqual(gridChallenge(['zxy']), "YES")

    def test_give_single_column_sorted_should_be_YES(self):
        self.assertEqual(gridChallenge(['a', 'b', 'c']), "YES")

    def test_give_single_column_unsorted_should_be_NO(self):
        self.assertEqual(gridChallenge(['c', 'b', 'a']), "NO")

if __name__ == '__main__':
    unittest.main()