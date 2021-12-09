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
    def has_left_child(self):
        if (self.left_child!=None):
            return True
    def has_right_child(self):
        if (self.right_child != None):
            return True
    def add_left_child(self, value: Any):
        self.left_child=BinaryNode(value)
    def add_right_child(self, value: Any):
        self.right_child=BinaryNode(value)
    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.has_left_child()==True:
            self.left_child.traverse_in_order(0)
        print(self)
        if self.has_right_child()==True:
            self.right_child.traverse_in_order(0)
    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.has_left_child() == True:
            self.left_child.traverse_post_order(0)
        if self.has_right_child() == True:
            self.right_child.traverse_post_order(0)
        print(self)
    def traverse_pre_order(self, visit: Callable[[Any], None]):
        print (self)
        if self.has_left_child() == True:
            self.left_child.traverse_pre_order(0)
        if self.has_right_child() == True:
            self.right_child.traverse_pre_order(0)
    def __str__ (self) -> str:
        return str(self.value)
    def show_auxiliary(root, string):
        print(string +" = " + str(root.value) +"\n")
        if root.has_left_child():
            root.left_child.show_auxiliary( (string + " left child"))
        if root.has_right_child():
            root.right_child.show_auxiliary( string + " right child")
class BinaryTree:
    root:BinaryNode
    def __init__(self, root):
        self.root=BinaryNode(root)
    def traverse_in_order(self, visit: Callable[[Any], None]):
        (self.root).traverse_in_order(0)
    def traverse_post_order(self, visit: Callable[[Any], None]):
        (self.root).traverse_post_order(0)
    def traverse_pre_order(self, visit: Callable[[Any], None]):
        (self.root).traverse_pre_order(0)
    def show(self):
        root=self.root
        string=("root")
        root.show_auxiliary(string)
def print_path(root, counter):
    list_of_specific_sums =[]
    if counter ==0:
        print(root.value)
    if root.has_left_child():
        print(root.left_child.value)
        print_path(root.left_child,1)
    if root.has_right_child():
        print(root.right_child.value)
        print_path(root.right_child,1)
def all_paths(root,list,blist):
    list.append(root)
    if root.has_left_child():
        all_paths(root.left_child,list.copy(),blist)
    if root.has_right_child():
        all_paths(root.right_child,list.copy(),blist)
    if root.is_leaf()==True:
        blist.append(list)
    return blist
def all_paths_on_special_circumstances(root,list,blist, lever):
    list.append(root)
    if root.has_left_child():
        all_paths_on_special_circumstances(root.left_child,list.copy(),blist,False)
    if root.has_right_child():
        all_paths_on_special_circumstances(root.right_child,list.copy(),blist,False)
    if root.is_leaf()==True:
        blist.append(list)
    if lever == True:
        return blist
def all_equal_paths_on_special_circumstances(tree: BinaryTree, sum_value: Any):
    result=[]
    for x in all_paths_on_special_circumstances(tree.root,[],[],True):
        sum=0
        for y in x:
            sum+=y.value
            #print(y.value)
        if sum==sum_value:
            #print("zgodne z suma")
            result.append(x)
    return result
def all_paths_values(root,list,blist):
    list.append(root.value)
    if root.has_left_child():
        all_paths_values(root.left_child,list.copy(),blist)
    if root.has_right_child():
        all_paths_values(root.right_child,list.copy(),blist)
    if root.is_leaf()==True:
        blist.append(list)
    return blist
def all_equal_paths(tree: BinaryTree, sum_value: Any):
    wynik=[]
    for x in all_paths(tree.root,[],[]):
        sum=0
        for y in x:
            sum+=y.value
            #print(y.value)
        if sum==sum_value:
            #print("zgodne z suma")
            wynik.append(x)
    return wynik
def all_equal_paths_values(tree: BinaryTree, sum_value: Any):
    wynik=[]
    for x in all_paths_values(tree.root,[],[]):
        sum=0
        for y in x:
            sum+=y
            #print(y.value)
        if sum==sum_value:
            #print("zgodne z suma")
            wynik.append(x)
    return wynik
#def all_equal_paths(tree: BinaryTree, sum_value: Any) ->List[List[BinaryNode]]:
 #   return 0
#print_path(tree.root,0)
#print(all_paths(tree.root,[],[]))
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
tree.root.right_child.add_left_child(4)
tree.root.left_child.add_right_child(5)
print(all_paths(tree.root,[],[]))
drzewo = BinaryTree(10)
drzewo1 = BinaryTree(1)
drzewo1.root.add_left_child(2)
drzewo1.root.add_right_child(3)
drzewo1.root.left_child.add_left_child(7)
drzewo1.root.left_child.add_right_child(5)
drzewo1.root.right_child.add_left_child(6)
drzewo1.root.right_child.add_right_child(7)
print(all_paths(drzewo.root,[],[]))
print(all_equal_paths(drzewo,10))
print(all_equal_paths(drzewo1,10))
print(all_equal_paths_values(drzewo,10))
print(all_equal_paths_values(tree,16))
print(all_equal_paths_values(drzewo1,10))
drzewo1.traverse_pre_order(0)
drzewo1.show()
print(all_equal_paths(tree,16))
print(all_equal_paths_on_special_circumstances(tree,16))


