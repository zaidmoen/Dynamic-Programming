# Dynamic Programming Cheat Sheet

Use this guide to move from a problem statement to a working recurrence.

## The five-question checklist

1. **State:** What information uniquely identifies a subproblem?
2. **Meaning:** What exactly does `dp[state]` store?
3. **Transition:** Which smaller states produce the current answer?
4. **Base case:** What are the smallest answers known immediately?
5. **Order:** In what order must states be evaluated?

## Memoization vs. tabulation

| Style | Direction | Best when | Main trade-off |
|---|---|---|---|
| Memoization | Top-down recursion | Only some states are needed | Recursion-stack overhead |
| Tabulation | Bottom-up iteration | Most states are needed | Must determine evaluation order |
| Space optimized | Bottom-up with rolling state | Only recent rows/states are needed | Harder reconstruction |

## Common patterns

| Pattern | Typical state | Example in this repository |
|---|---|---|
| Linear sequence | `dp[i]` | Fibonacci |
| Capacity / choice | `dp[i][capacity]` | 0/1 Knapsack |
| Unbounded choice | `dp[amount]` | Coin Change |
| Two sequences | `dp[i][j]` | LCS, Edit Distance |
| Grid | `dp[row][column]` | Unique Paths |
| Best subsequence | Best result ending at `i` | LIS |

## A practical workflow

Start with a correct recursive definition. Add memoization to confirm the state,
then convert it to tabulation if you need tighter control over performance.
Finally, inspect each transition: if it reads only the previous row or a few
previous values, compress the DP table.

## Complexity rule of thumb

> Time complexity is usually the number of states multiplied by the work per
> transition. Space complexity is the number of stored states.

## Common mistakes

- Using a state that does not contain enough information.
- Updating a one-dimensional table in the wrong direction.
- Forgetting impossible states or empty-input base cases.
- Confusing combinations with permutations in Coin Change.
- Optimizing space before the recurrence is correct.
- Returning only the score when the problem requires reconstruction.
