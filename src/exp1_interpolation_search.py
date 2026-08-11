"""Experiment 1: Interpolation Search."""

from typing import List


def interpolation_search(arr: List[int], target: int) -> int:
    """Return the index of target in a sorted array using interpolation search.

    Assumes arr is sorted in ascending order and contains unique values.
    """
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if arr[low] == arr[high]:
            return low if arr[low] == target else -1

        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if pos < low or pos > high:
            return -1

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


def demo():
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target = 70
    result = interpolation_search(data, target)

    print("Experiment 1: Interpolation Search")
    print("Sorted data:", data)
    print(f"Search for {target}: index {result}")

    if result != -1:
        print("Element found successfully.")
    else:
        print("Element not found.")


if __name__ == "__main__":
    demo()
