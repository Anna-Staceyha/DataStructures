head = 0
name = 0 
pointer = 1
maxCounter = 4

LinkedList = [
    ["Bob", 3],
    ["Sarah", 2],
    ["Sharon", None],
    ["Roberto", 1],
    [None, None],
    [None, None]
]

maxItems = len(LinkedList)

def traverseList():
    global current
    # Check if the list is empty
    if head == None:
        print("The list is empty")
    else:
        # If it is not empty print list
        current = head
        while current != None:
            print(LinkedList[current][name])
            current = LinkedList[current][pointer]

  
# Add data to node using a function
'''
check that there is free space in the array
traverse the list to find the end of the list (this will be the element whose next_position index pointer has the value Null)
store the new item in the free space found; this item is now the end of the list
adjust the next_position index pointer of the element that was previously last in the list
'''
def AddNode(data):
    global name, maxItens, maxCounter, head, current, pointer
    #check that there is free space in the array
    if maxCounter == maxItems:
        print("Error: List is full")
    else:
        print("List is not full")
        traverseList()
        # Assign data to a new node
        new_node = data
        # If there is no data in the head then add new node as the head 
        if LinkedList[head] is None:
            new_node = LinkedList[head]
            pointer = pointer + 1
            print(LinkedList)
        else:
            new_node = LinkedList[name]
            print(LinkedList)
            pointer = pointer + 1




