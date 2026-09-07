"""Levenshtein edit distance using bottom-up dynamic programming."""


def edit_distance(source: str, target: str) -> int:
    """Return the minimum inserts, deletes, and replacements required.

    Time complexity: O(len(source) * len(target))
    Space complexity: O(min(len(source), len(target)))
    """
    if len(source) < len(target):
        source, target = target, source

    previous = list(range(len(target) + 1))

    for source_index, source_character in enumerate(source, start=1):
        current = [source_index]

        for target_index, target_character in enumerate(target, start=1):
            insertion = current[target_index - 1] + 1
            deletion = previous[target_index] + 1
            replacement = previous[target_index - 1] + (
                source_character != target_character
            )
            current.append(min(insertion, deletion, replacement))

        previous = current

    return previous[-1]


if __name__ == "__main__":
    print(f"kitten -> sitting: {edit_distance('kitten', 'sitting')}")
