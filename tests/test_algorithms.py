"""Regression tests for the algorithm collection."""

import unittest

from coin_change.coin_change import count_combinations, minimum_coins
from divide_and_conquer.divide_and_conquer import binary_search, merge_sort
from edit_distance.edit_distance import edit_distance
from fibonacci.fibonacci import fibonacci_memoized, fibonacci_tabulated
from grid_paths.grid_paths import unique_paths
from knapsack.knapsack import knapsack_01
from longest_common_subsequence.lcs import longest_common_subsequence
from longest_increasing_subsequence.lis import longest_increasing_subsequence
from trees.binary_search_tree import BinarySearchTree


class DynamicProgrammingTests(unittest.TestCase):
    def test_fibonacci_implementations_agree(self) -> None:
        for n in range(25):
            self.assertEqual(fibonacci_memoized(n), fibonacci_tabulated(n))
        self.assertEqual(fibonacci_tabulated(10), 55)

    def test_knapsack_returns_best_value_and_items(self) -> None:
        value, selected = knapsack_01([2, 3, 4, 5], [3, 4, 5, 6], 5)
        self.assertEqual(value, 7)
        self.assertEqual(selected, [0, 1])

    def test_coin_change_variants(self) -> None:
        self.assertEqual(minimum_coins([1, 2, 5], 11), 3)
        self.assertEqual(minimum_coins([2], 3), -1)
        self.assertEqual(count_combinations([1, 2, 5], 5), 4)

    def test_sequence_algorithms(self) -> None:
        length, sequence = longest_common_subsequence("AGGTAB", "GXTXAYB")
        self.assertEqual((length, sequence), (4, "GTAB"))

        length, sequence = longest_increasing_subsequence(
            [10, 9, 2, 5, 3, 7, 101, 18]
        )
        self.assertEqual(length, 4)
        self.assertEqual(sequence, sorted(sequence))
        self.assertEqual(len(set(sequence)), length)

    def test_edit_distance(self) -> None:
        self.assertEqual(edit_distance("kitten", "sitting"), 3)
        self.assertEqual(edit_distance("", "abc"), 3)
        self.assertEqual(edit_distance("dynamic", "dynamic"), 0)

    def test_grid_paths(self) -> None:
        self.assertEqual(unique_paths(3, 7), 28)
        self.assertEqual(unique_paths(3, 3, {(1, 1)}), 2)
        self.assertEqual(unique_paths(2, 2, {(0, 0)}), 0)


class SupportingAlgorithmTests(unittest.TestCase):
    def test_divide_and_conquer(self) -> None:
        values = [38, 27, 43, 3, 9, 82, 10]
        sorted_values = merge_sort(values)
        self.assertEqual(sorted_values, sorted(values))
        self.assertEqual(binary_search(sorted_values, 43), 5)
        self.assertEqual(binary_search(sorted_values, 100), -1)

    def test_binary_search_tree(self) -> None:
        tree = BinarySearchTree()
        for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
            tree.insert(value)

        self.assertEqual(tree.inorder(), [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertTrue(tree.contains(7))
        self.assertFalse(tree.contains(99))
        self.assertEqual(tree.height(), 4)


if __name__ == "__main__":
    unittest.main()
