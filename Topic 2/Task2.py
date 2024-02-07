queue = ["","","","",""]

def enqueue(personName):
    if len(queue) < 5:
        queue[0] = [personName]
    else:
        print("Error Full")

def dequeue():
    if len(queue) > 0:
        removed_personName = queue[-1]
        queue = queue[-1]
        return removed_personName
    else:
        print("Error Full")
        return None
    
def isFull():
    return len(queue) == 5

def isEmpty():
    return len(queue) == 0

enqueue("A")
enqueue("B")
dequeue("C")

return_personName = dequeue()