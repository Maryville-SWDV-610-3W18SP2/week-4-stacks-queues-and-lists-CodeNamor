#F. Derek Roman - GitHub Profile CodeNamor
#SWDV-610-3W - Data Structures
#Unit 4 Assignment -       I Attest that this is my own work

class Deque:
    #constructor to implement a linked list
    def __init__(self):
        self.deque=list()
    
    #adding a new element to the Deque
    def addFront(self, data):
    #check to avoid duplicate entries
        if data not in self.deque:
            self.deque.append(data)
            return True
        return False
    
    #remove last element from the Deque
    def removeFront(self):
        if len(self.deque)<=0:
            return("Deque Empty!")
        return self.deque.pop()
    
    #Getting the size of the Deque
    def size(self):
        return len(self.deque)
    
myDeque = Deque()
print(myDeque.addFront(19)) #prints True
print(myDeque.addFront(20))
print(myDeque.addFront(18))
print(myDeque.addFront(19)) #prints False
print(myDeque.size())
print(myDeque.removeFront())
print(myDeque.removeFront())
print(myDeque.removeFront())
print(myDeque.size())
print(myDeque.removeFront())
