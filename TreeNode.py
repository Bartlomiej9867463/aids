from typing import Any, List, Callable


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value = None):
        self.value = value
        self.children = []

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True
        else:
            return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)







