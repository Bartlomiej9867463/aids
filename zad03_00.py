from typing import Any

class Node:
    value: Any
    next: 'Node'
    def __init__(self, value,next):
        self.value = value
        self.next = next
class LinkedList:
    head: Node=None
    tail: Node=None
    def push(self, value: Any) -> None:
        if self.head == None:
            self.head = Node(value,self.tail)
            # print(self.head.value)
            self.tail= None
        elif self.head != None:
            buforek=self.head
            self.head = Node(value,buforek)
            # print(self.head.value)
            self.tail= None
    def append(self, value: Any) -> None :
        if self.head == None:
            self.head = Node(value, self.tail)
            # print(self.head.value)
            self.tail = None
        elif self.head.next != None:
            scope = self.head
            while ((scope.next).next != None):
                # print("test print")
                scope = scope.next
            (scope.next).next = Node(value,self.tail)
    def node(self, at: int) -> Node:
        pozycja =0
        if self.head == None:
            return None
        scope = self.head
        if (at==0):
            return self.head
        while (pozycja+1!=at):
            pozycja+=1
            scope = scope.next
        return scope.next
    def insert(self, value: Any, after: Node) -> None:
         if self.head == None:
             self.head = Node(value, self.tail)
             # print(self.head.value)
             self.tail = None
         elif after.next == self.tail:
             after.next=Node(value,self.tail)
         elif self.head.next != None:
             schowek =(after.next).next
             after.next = Node(value,schowek)
    def pop(self) -> Any :
        if self.head == None:
            self.head = None
        elif self.head.next == None:
            schowek = self.head.value
            self.head=None
            return schowek
        else:
            schowek = self.head.value
            self.head = self.head.next
            return schowek
    def remove_last(self) -> Any :
        tymczas=None
        wynik=0
        # brak zabezpieczenia przed usunieciem jedynegho wyniku
        if self.head == None:
            self.head = None
        elif self.head.next == None:
            # print(self.head)
            schowek = self.head
            self.head = None
            # print(self.head)
            return schowek.value
        else:
            tymczas = self.head
            wynik = (tymczas.next).value
            while ((tymczas.next).next != None):
                tymczas = tymczas.next
                wynik = (tymczas.next).value
            (tymczas.next) = None

            return wynik
    def remove(self, after: Node) -> Any:
        if self.head == None:
            self.head = None
        elif after.next == self.tail:
            schowek = self.head
            self.head = None
            # print(self.head)
            return schowek.value
        else:
            print("test")
            schowek = (after.next)
            after.next = (after.next).next
            return schowek.value
    def __len__(self) -> int:
        zwracacz = 0
        # print(self.head)
        scope = self.head
        while (scope != None):
            zwracacz+=1
            scope = scope.next
        return zwracacz
    def __str__ (self) -> str:
        zwracacz=""
        scope = self.head
        # print(self.head.value)
        # print(scope)
        if scope==None:
            return "None"
        while(scope != None):
            # print(scope)
            zwracacz+=str(scope.value)
            zwracacz +=" -> "
            scope=scope.next
        zwracacz = zwracacz[:-4]
        return zwracacz
class Stack:
    _storage: LinkedList
    def __init__(self):
        self.element = LinkedList()
    def push(self, element: Any) -> None:
        (self.element).push(element)
    def pop(self) -> Any:
        pass
    def __len__(self) -> int:
        zwracacz = 0
        scope = self.element.head
        print(scope)
        # jeju jakie okropne rozwiazanie tego buga
        if str(scope)=="None":
            return 0
        else:
            while (scope != None):
                zwracacz+=1
                scope = scope.next
            return zwracacz
    # def __str__ (self) -> str:
    #     zwracacz=""
    #     scope = self.head
    #     # print(self.head.value)
    #     # print(scope)
    #     if scope==None:
    #         return "None"
    #     while(scope != None):
    #         # print(scope)
    #         zwracacz+=str(scope.value)
    #         zwracacz +=" -> "
    #         scope=scope.next
    #     zwracacz = zwracacz[:-4]
    #     return zwracacz
list_ = LinkedList()
assert list_.head == None
list_.push(1)
# print(list_)
list_.push(1)
# print(list_)
list_.append(2)
list_.append(1)
print(list_)
middle_node=(list_.node(1))
print(middle_node)
list_.insert(5, middle_node)
print(list_)
print(list_.pop())
print(list_)
print(list_.remove_last())
print(list_)
print(list_.remove(middle_node))
print(list_)
stack = Stack()
assert len(stack) == 0
stack.push(3)
stack.push(3)
stack.push(3)
print(len(stack))
#wezel 0 buguje





