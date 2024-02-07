class NodeRecord():
    def __init__(self):
        self.data = None
        self.next = None

# Initialise to None as the linked list is empty
head = None

class Node():
    def __init__(self, given_data):
        """Constructor method"""
        self.data = given_data
        self.next = None
    
# Getters and setters
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    # Pointer for node
    def set_next(self,new_next):
        self.next = new_next

class LinkedList():
    def __init__(self):
      """Constructor method"""
      self.head = None

    def get_head(self):
        return self.head
      
    def set_head(self,new_head):
        self.head = new_head

    def insert_at_front(self, data):
        # Create a new node
        new_node = Node(data)

        # Check if the head node exists
        if self.get_head() is None:      # If there is no head node set the new node as the head node
            self.set_head = (new_node)
        else:
            # If there is already a head node update the pointers so the new node is the head
            new_node.set_next(self.head())
            self.set_head = (new_node)

    def insert_in_order(self, data):
            """Insert a node into the correct position in an ordered list"""

            # Create a new node
            new_node = Node(data)

            # Start at the head of the list
            current = self.get_head()
            
            # Check if there are no nodes in the list
            if current is None:
                self.set_head(new_node)

            # Check if the new node data is before the head data
            elif new_node.get_data() < current.get_data():
                # Set the new node as the head of the list
                new_node.set_next(self.get_head())
                self.set_head(new_node)

            # Otherwise find where the new node should be positioned
            else:
                # Repeat until the point of insertion is found
                while (current.get_next() is not None
                    and current.get_next().get_data() < new_node.get_data()):
                    # Get the next node
                    current = current.get_next()

                # Update the pointers of the new and current nodes
                new_node.set_next(current.get_next())
                current.set_next(new_node)


    # Procedure to go through the list starting from the head 
    def traverse (self):
        #set the current node as the head
        current = self.get_head()
        # Repeat until next pointer is null - if head == null the list is empty
        while current is not None:
            print(current.get_data())
            current = current.get_next()
            
