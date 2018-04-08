#F. Derek Roman - GitHub Profile CodeNamor
#SWDV-610-3W - Data Structures
#Unit 4 Assignment -       I Attest that this is my own work

class Stack:
    #Constructor creates a list
    def __init__(self):
        self.stack = list()
        
    #Adding elements to stack
    def push(self, data):
        #check to avoid duplicate entries
        if data not in self.stack:
            self.stack.append(data)
            return True
        return False
    
    #remove last element from the stack
    def pop(self):
        if len(self.stack)<=0:
            return("Stack Empty!")
        return self.stack.pop()
    
    #Getting the size of the stack
    def size(self):
        return len(self.stack)
        
myStack = Stack()
print(myStack.push('new')) #prints True
print(myStack.push('car'))
print(myStack.push(18))
print(myStack.push('new')) #prints False
print(myStack.size())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.size())
print(myStack.pop())