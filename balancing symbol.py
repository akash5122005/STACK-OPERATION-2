class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head is None

    def push(self,data):
        newnode=node(data)
        newnode.next=self.head 
        self.head=newnode

    def pop(self):
        popped_node=self.head.data
        self.head=self.head.next
        return popped_node

    def peek(self):
        return self.head.data

def matchpair(opening,close):
    pairs={")":"(","]":"[","}":"{"}

    return pairs.get(close) == opening

def check(exp):
    stack=Stack()

    for char in exp:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty() or not matchpair(stack.pop(),char):
                return "Not Balanced"

    return "Balanced" if stack.is_empty() else "Not Balanced"

n=int(input())
for i in range(n):
    exp=input()
    r=check(exp)
    print(r)                                                       
