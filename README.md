<div align="center">

![Dynamic Programming Header](https://capsule-render.vercel.app/api?type=waving&color=0:0F172A,50:2563EB,100:22D3EE&height=220&section=header&text=Dynamic%20Programming&fontSize=46&fontColor=FFFFFF&animation=fadeIn&fontAlignY=38&desc=Learn%20patterns.%20Solve%20problems.%20Build%20intuition.&descAlignY=58&descSize=18)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&pause=1000&color=38BDF8&center=true&vCenter=true&width=760&lines=Dynamic+Programming+%7C+Divide+%26+Conquer+%7C+Trees;Clean+Python+solutions+with+complexity+analysis;From+core+ideas+to+classic+interview+problems)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Algorithms](https://img.shields.io/badge/Algorithms-Learning-2563EB?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-22C55E?style=for-the-badge)

</div>

## About

A structured collection of classic algorithms implemented in Python. Each
example favors readable code, clear return values, input validation, and
time/space complexity notes.

## Topics

| Topic | Core idea | Complexity | Implementation |
|---|---|---:|---|
| 0/1 Knapsack | Choose the best-value item set within a capacity | O(n × capacity) | [\x60knapsack.py\x60](knapsack/knapsack.py) |
| Divide & Conquer | Split, solve smaller parts, and combine | O(n log n) for merge sort | [\x60divide_and_conquer.py\x60](divide_and_conquer/divide_and_conquer.py) |
| Binary Search Tree | Store ordered values for efficient lookup | O(h) average operation | [\x60binary_search_tree.py\x60](trees/binary_search_tree.py) |
| Longest Common Subsequence | Find the longest ordered match | O(m × n) | [\x60lcs.py\x60](longest_common_subsequence/lcs.py) |
| Coin Change | Minimize coins or count combinations | O(amount × coins) | [\x60coin_change.py\x60](coin_change/coin_change.py) |

## How Dynamic Programming Works

\x60\x60\x60mermaid
flowchart TD
    A[Start with a problem] --> B{Repeated subproblems?}
    B -- No --> C[Use another technique]
    B -- Yes --> D{Optimal substructure?}
    D -- No --> C
    D -- Yes --> E[Define the state]
    E --> F[Build a recurrence]
    F --> G[Memoization or tabulation]
    G --> H[Return the final state]
\x60\x60\x60

Dynamic programming becomes useful when the same smaller problems appear
repeatedly and their answers can be combined to solve the original problem.

## Repository Structure

\x60\x60\x60text
Dynamic-Programming/
├── knapsack/
│   └── knapsack.py
├── divide_and_conquer/
│   └── divide_and_conquer.py
├── trees/
│   └── binary_search_tree.py
├── longest_common_subsequence/
│   └── lcs.py
├── coin_change/
│   └── coin_change.py
└── README.md
\x60\x60\x60

## Run the Examples

Clone the repository and run any topic directly:

\x60\x60\x60bash
git clone https://github.com/zaidmoen/Dynamic-Programming.git
cd Dynamic-Programming
python knapsack/knapsack.py
python divide_and_conquer/divide_and_conquer.py
python trees/binary_search_tree.py
python longest_common_subsequence/lcs.py
python coin_change/coin_change.py
\x60\x60\x60

No external packages are required.

## Learning Path

1. Start with **Divide & Conquer** to understand recursive decomposition.
2. Practice **Trees** to become comfortable with recursive structures.
3. Learn DP state and transitions with **Coin Change**.
4. Move to two-dimensional DP with **Knapsack**.
5. Finish with **Longest Common Subsequence** and solution reconstruction.

## Contributing

Contributions are welcome. Keep implementations readable, document their
complexities, and include a small runnable example.

---

<div align="center">
Built for consistent algorithm practice and stronger problem-solving skills.
</div>
