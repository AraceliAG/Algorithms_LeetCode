
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val #number
        self.next = next

class LinkedList:
    def __init__(self):
        self.head=None
    
    #INSERT start 
    def insert_node_at_start(self, val):
        new_node = ListNode(val)
        if (self.head is None):
            self.head = new_node
            return
    
        #head 
        new_node.next =self.head
        self.head = new_node
        
    def insert_node_at_end (self, val):
        new_node = ListNode(val)
        if (self.head == None):
            self.head = new_node
            return

        #insert head (end)
        current = self.head #
        while(current.next):
            current = current.next
        
        current.next = new_node 
            
    def print_linked_list(self):
        current = self.head
        while current:
            print(current.val, "-->", end=" ")
            current = current.next
        
    def delete_at_start(self):
        if(self.head is None):
            print("there aren't elements to delete")
            return
        self.head = self.head.next
    
    def delete_at_end(self):
        
        if(self.head is None):
            print("there aren't elements to delete")
            return
        
        if(self.head.next is None):
            self.head = None
            return
        current = self.head
        
        while current.next.next:
            current= current.next
        current.next = None
    def exist(self, var):
        if(self.head is None):
            print("empty list")
            return False
        current=self.head
        while(current.val != var):
            current=current.next
            if current is None:
                return False
        return True

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next   # save next node
            current.next = prev        # Inv
            prev = current             # move prev to current
            current = next_node        # advance to the next
        self.head = prev               # new head
    
    @staticmethod
    def sum_linked_lists(list1, list2):
        result = LinkedList()

        current1 = list1.head
        current2 = list2.head

        while current1 or current2:
            val1 = current1.val if current1 else 0
            val2 = current2.val if current2 else 0
            result.insert_node_at_end(val1 + val2)

            if current1:
                current1 = current1.next
            if current2:
                current2 = current2.next

        return result




list1 = LinkedList()
list2 = LinkedList()


list1.insert_node_at_start(1)
list1.insert_node_at_end(2)
list1.insert_node_at_end(3)
list1.insert_node_at_start(9)


# Insert element in the second list
list2.insert_node_at_start(10)
list2.insert_node_at_end(20)
list2.insert_node_at_end(30)

# print both list
print("List 1:")
list1.print_linked_list()
print("\List 2:")
list2.print_linked_list()

sum_list = LinkedList.sum_linked_lists(list1, list2)

# sum_list = sum_linked_lists(list1, list2)
print("Result of sum:")
sum_list.print_linked_list()