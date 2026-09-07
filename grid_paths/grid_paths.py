"""Count unique paths through a rectangular grid with optional obstacles."""


def unique_paths(
    rows: int,
    columns: int,
    blocked: set[tuple[int, int]] | None = None,
) -> int:
    """Return the number of paths from top-left to bottom-right.

    Movement is limited to right and down. Blocked cells use zero-based
    (row, column) coordinates.

    Time complexity: O(rows * columns)
    Space complexity: O(columns)
    """
    if rows <= 0 or columns <= 0:
        raise ValueError("rows and columns must be positive")

    obstacles = blocked or set()
    for row, column in obstacles:
        if not (0 <= row < rows and 0 <= column < columns):
            raise ValueError("blocked cell is outside the grid")

    dp = [0] * columns
    dp[0] = 1

    for row in range(rows):
        for column in range(columns):
            if (row, column) in obstacles:
                dp[column] = 0
            elif column > 0:
                dp[column] += dp[column - 1]

    return dp[-1]


if __name__ == "__main__":
    print(f"3 x 7 grid: {unique_paths(3, 7)}")
    print(f"3 x 3 with center blocked: {unique_paths(3, 3, {(1, 1)})}")
