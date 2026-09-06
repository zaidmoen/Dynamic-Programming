"""Two common Coin Change problems solved with dynamic programming."""


def minimum_coins(coins: list[int], amount: int) -> int:
    """Return the minimum coins needed, or -1 when amount is impossible.

    Time complexity: O(amount * number_of_coins)
    Space complexity: O(amount)
    """
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if any(coin <= 0 for coin in coins):
        raise ValueError("coin values must be positive")

    impossible = amount + 1
    dp = [0] + [impossible] * amount

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(
                    dp[current_amount],
                    1 + dp[current_amount - coin],
                )

    return -1 if dp[amount] == impossible else dp[amount]


def count_combinations(coins: list[int], amount: int) -> int:
    """Return how many unordered coin combinations make the amount."""
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if any(coin <= 0 for coin in coins):
        raise ValueError("coin values must be positive")

    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for current_amount in range(coin, amount + 1):
            dp[current_amount] += dp[current_amount - coin]

    return dp[amount]


if __name__ == "__main__":
    sample_coins = [1, 2, 5]
    sample_amount = 11

    print(f"Minimum coins: {minimum_coins(sample_coins, sample_amount)}")
    print(f"Combinations for 5: {count_combinations(sample_coins, 5)}")
