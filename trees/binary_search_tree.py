"""A small Binary Search Tree implementation with common operations."""

from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: "Node | None" = None
    right: "Node | None" = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def insert(self, value: int) -> None:
        """Insert value into the tree. Duplicate values are ignored."""
        self.root = self._insert(self.root, value)

    def _insert(self, node: Node | None, value: int) -> Node:
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node

    def contains(self, value: int) -> bool:
        """Return whether value exists in the tree."""
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def inorder(self) -> list[int]:
        """Return values in ascending order."""
        result: list[int] = []

        def traverse(node: Node | None) -> None:
            if node is None:
                return
            traverse(node.left)
            result.append(node.value)
            traverse(node.right)

        traverse(self.root)
        return result

    def preorder(self) -> list[int]:
        """Return values using root-left-right traversal."""
        result: list[int] = []

        def traverse(node: Node | None) -> None:
            if node is None:
                return
            result.append(node.value)
            traverse(node.left)
            traverse(node.right)

        traverse(self.root)
        return result

    def postorder(self) -> list[int]:
        """Return values using left-right-root traversal."""
        result: list[int] = []

        def traverse(node: Node | None) -> None:
            if node is None:
                return
            traverse(node.left)
            traverse(node.right)
            result.append(node.value)

        traverse(self.root)
        return result

    def height(self) -> int:
        """Return the number of levels in the tree."""
        def node_height(node: Node | None) -> int:
            if node is None:
                return 0
            return 1 + max(node_height(node.left), node_height(node.right))

        return node_height(self.root)


if __name__ == "__main__":
    tree = BinarySearchTree()
    for number in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        tree.insert(number)

    print(f"Inorder: {tree.inorder()}")
    print(f"Preorder: {tree.preorder()}")
    print(f"Postorder: {tree.postorder()}")
    print(f"Contains 7: {tree.contains(7)}")
    print(f"Height: {tree.height()}")
