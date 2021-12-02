from typing import Any, Callable

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'
    def __init__(self,value):
        self.value=value
        self.left_child=None
        self.right_child=None
    def is_leaf(self):
        if ((self.left_child==None)&(self.right_child==None)):
            return True
        else:
            return False
    def add_left_child(self, value: Any):
        self.left_child=BinaryNode(value)
    def add_right_child(self, value: Any):
        self.right_child=BinaryNode(value)
class BinaryTree:
    root:BinaryNode
    def __init__(self, root):
        self.root=BinaryNode(root)
    def traverse_in_order(self, visit: Callable[[Any], None]):
        return 0
    def traverse_post_order(self, visit: Callable[[Any], None]):
        return 0
    def traverse_pre_order(self, visit: Callable[[Any], None]):
        return 0
    def show(self):
        return 0
tree = BinaryTree(10)
assert tree.root.value == 10
tree.root.add_right_child(2)
assert tree.root.right_child.value == 2
tree.root.right_child.add_right_child(2)
assert tree.root.is_leaf() is False
tree.root.add_left_child(1)
tree.root.left_child.add_left_child(1)
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True
