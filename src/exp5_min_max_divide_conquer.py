"""Experiment 5: Min-Max using divide and conquer."""


def min_max_divide_conquer(arr):
    """Return (minimum, maximum) using divide and conquer."""
    if len(arr) == 1:
        return arr[0], arr[0]

    if len(arr) == 2:
        return (min(arr), max(arr))

    mid = len(arr) // 2
    left_min, left_max = min_max_divide_conquer(arr[:mid])
    right_min, right_max = min_max_divide_conquer(arr[mid:])

    return min(left_min, right_min), max(left_max, right_max)


def demo():
    data = [7, 2, 9, 3, 1, 6, 8, 5, 4]
    min_value, max_value = min_max_divide_conquer(data)

    print("Experiment 5: Min-Max by Divide and Conquer")
    print("Array:", data)
    print(f"Minimum: {min_value}")
    print(f"Maximum: {max_value}")


if __name__ == "__main__":
    demo()
