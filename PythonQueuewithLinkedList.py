#F. Derek Roman - GitHub Profile CodeNamor
#SWDV-610-3W - Data Structures
#Unit 4 Assignment -       I Attest that this is my own work

class Queue:
    #constructor to implement a linked list
    def __init__(self):
        self.queue=list()
    
    #adding a new element to the queue
    def enqueue(self, data):
    #check to avoid duplicate entries
        if data not in self.queue:
            self.queue.append(data)
            return True
        return False
    
    #remove last element from the queue
    def pop(self):
        if len(self.queue)<=0:
            return("Queue Empty!")
        return self.queue.pop()
    
    #Getting the size of the queue
    def size(self):
        return len(self.queue)
    
myQueue = Queue()
print(myQueue.enqueue(19)) #prints True
print(myQueue.enqueue(20))
print(myQueue.enqueue(18))
print(myQueue.enqueue(19)) #prints False
print(myQueue.size())
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.size())
print(myQueue.pop())