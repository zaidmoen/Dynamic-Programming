"""0/1 Knapsack solved with dynamic programming.

Each item may be selected at most once. The function returns both the maximum
value and the indices of the selected items.
"""


def knapsack_01(weights: list[int], values: list[int], capacity: int) -> tuple[int, list[int]]:
    """Return the maximum value and selected item indices.

    Time complexity: O(n * capacity)
    Space complexity: O(n * capacity)
    """
    if len(weights) != len(values):
        raise ValueError("weights and values must have the same length")
    if capacity < 0 or any(weight < 0 for weight in weights):
        raise ValueError("capacity and weights must be non-negative")

    item_count = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(item_count + 1)]

    for item in range(1, item_count + 1):
        weight = weights[item - 1]
        value = values[item - 1]

        for current_capacity in range(capacity + 1):
            dp[item][current_capacity] = dp[item - 1][current_capacity]
            if weight <= current_capacity:
                dp[item][current_capacity] = max(
                    dp[item][current_capacity],
                    value + dp[item - 1][current_capacity - weight],
                )

    selected_items: list[int] = []
    current_capacity = capacity

    for item in range(item_count, 0, -1):
        if dp[item][current_capacity] != dp[item - 1][current_capacity]:
            selected_items.append(item - 1)
            current_capacity -= weights[item - 1]

    selected_items.reverse()
    return dp[item_count][capacity], selected_items


if __name__ == "__main__":
    sample_weights = [2, 3, 4, 5]
    sample_values = [3, 4, 5, 6]
    best_value, chosen = knapsack_01(sample_weights, sample_values, capacity=5)

    print(f"Maximum value: {best_value}")
    print(f"Selected item indices: {chosen}")
