class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_node_at_start(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        
    def insert_node_at_end(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node 
            
    def print_linked_list(self):
        current = self.head
        while current:
            print(current.val, "-->", end=" ")
            current = current.next
        print("None")
        
    def delete_at_start(self):
        if self.head:
            self.head = self.head.next
    
    def delete_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def exist(self, var):
        current = self.head
        while current:
            if current.val == var:
                return True
            current = current.next
        return False

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    @staticmethod
    def merge_linked_lists(list1, list2):
        # Ahora acepta LinkedList, no solo ListNode
        l1 = list1.head
        l2 = list2.head
        dummy = ListNode(0)
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
            
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list


# Ejemplo de uso
list1 = LinkedList()
list2 = LinkedList()

list1.insert_node_at_end(1)
list1.insert_node_at_end(2)
list1.insert_node_at_end(4)

list2.insert_node_at_end(1)
list2.insert_node_at_end(3)
list2.insert_node_at_end(4)

print("List 1:")
list1.print_linked_list()
print("List 2:")
list2.print_linked_list()

sum_list = LinkedList.merge_linked_lists(list1, list2)

print("Merged List:")
sum_list.print_linked_list()
