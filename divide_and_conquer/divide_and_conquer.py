"""Classic divide-and-conquer examples: merge sort and binary search."""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def merge_sort(items: Sequence[T]) -> list[T]:
    """Return a sorted copy of items in O(n log n) time."""
    if len(items) <= 1:
        return list(items)

    middle = len(items) // 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])
    return _merge(left, right)


def _merge(left: list[T], right: list[T]) -> list[T]:
    result: list[T] = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def binary_search(items: Sequence[T], target: T) -> int:
    """Return the target index in a sorted sequence, or -1 if absent."""
    low, high = 0, len(items) - 1

    while low <= high:
        middle = (low + high) // 2
        if items[middle] == target:
            return middle
        if items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1


if __name__ == "__main__":
    numbers = [38, 27, 43, 3, 9, 82, 10]
    sorted_numbers = merge_sort(numbers)

    print(f"Sorted: {sorted_numbers}")
    print(f"Index of 43: {binary_search(sorted_numbers, 43)}")
