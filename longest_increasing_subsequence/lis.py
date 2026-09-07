"""Longest Increasing Subsequence in O(n log n) time."""

from bisect import bisect_left
from collections.abc import Sequence


def longest_increasing_subsequence(numbers: Sequence[int]) -> tuple[int, list[int]]:
    """Return the LIS length and one valid strictly increasing subsequence.

    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    if not numbers:
        return 0, []

    tail_values: list[int] = []
    tail_indices: list[int] = []
    previous_indices = [-1] * len(numbers)

    for index, number in enumerate(numbers):
        position = bisect_left(tail_values, number)

        if position == len(tail_values):
            tail_values.append(number)
            tail_indices.append(index)
        else:
            tail_values[position] = number
            tail_indices[position] = index

        if position > 0:
            previous_indices[index] = tail_indices[position - 1]

    sequence: list[int] = []
    current_index = tail_indices[-1]

    while current_index != -1:
        sequence.append(numbers[current_index])
        current_index = previous_indices[current_index]

    sequence.reverse()
    return len(sequence), sequence


if __name__ == "__main__":
    length, sequence = longest_increasing_subsequence(
        [10, 9, 2, 5, 3, 7, 101, 18]
    )
    print(f"LIS length: {length}")
    print(f"LIS: {sequence}")
