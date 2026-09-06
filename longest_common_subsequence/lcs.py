"""Longest Common Subsequence using bottom-up dynamic programming."""


def longest_common_subsequence(first: str, second: str) -> tuple[int, str]:
    """Return the LCS length and one valid subsequence.

    Time complexity: O(m * n)
    Space complexity: O(m * n)
    """
    rows, columns = len(first) + 1, len(second) + 1
    dp = [[0] * columns for _ in range(rows)]

    for row in range(1, rows):
        for column in range(1, columns):
            if first[row - 1] == second[column - 1]:
                dp[row][column] = 1 + dp[row - 1][column - 1]
            else:
                dp[row][column] = max(dp[row - 1][column], dp[row][column - 1])

    characters: list[str] = []
    row, column = len(first), len(second)

    while row > 0 and column > 0:
        if first[row - 1] == second[column - 1]:
            characters.append(first[row - 1])
            row -= 1
            column -= 1
        elif dp[row - 1][column] >= dp[row][column - 1]:
            row -= 1
        else:
            column -= 1

    subsequence = "".join(reversed(characters))
    return dp[-1][-1], subsequence


if __name__ == "__main__":
    length, sequence = longest_common_subsequence("AGGTAB", "GXTXAYB")
    print(f"LCS length: {length}")
    print(f"LCS: {sequence}")
