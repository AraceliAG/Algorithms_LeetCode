# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val #number
        self.next = next

class LinkedList:
    def __init__(self):
        self.head=None
    
    #INSERT INICIO 
    def insert_node_at_start(self, val):
        new_node = ListNode(val)
        if (self.head is None):
            self.head = new_node
            return
    
        #cabeza apunte a nuevo (inicio)
        new_node.next =self.head
        self.head = new_node
        
    def insert_node_at_end (self, val):
        new_node = ListNode(val)
        if (self.head == None):
            self.head = new_node
            return

        #cabeza apunte a nuevo (final)
        current = self.head #lo que apunta(actual)
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
            print("no hay nada que eliminar")
            return
        self.head = self.head.next
    
    def delete_at_end(self):
        
        if(self.head is None):
            print("no hay nada que eliminar")
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
            print("lista vacia")
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
            next_node = current.next   # Guardas el siguiente nodo
            current.next = prev        # Inviertes el puntero
            prev = current             # Mueves prev a current
            current = next_node        # Avanzas al siguiente
        self.head = prev               # Nueva cabeza
    
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



# Crear dos listas enlazadas diferentes
list1 = LinkedList()
list2 = LinkedList()

# Insertar elementos en la primera lista
list1.insert_node_at_start(1)
list1.insert_node_at_end(2)
list1.insert_node_at_end(3)
list1.insert_node_at_start(9)


# Insertar elementos en la segunda lista
list2.insert_node_at_start(10)
list2.insert_node_at_end(20)
list2.insert_node_at_end(30)

# Imprimir ambas listas
print("Lista 1:")
list1.print_linked_list()
print("\nLista 2:")
list2.print_linked_list()

sum_list = LinkedList.sum_linked_lists(list1, list2)

# sum_list = sum_linked_lists(list1, list2)
print("Resultado de la suma:")
sum_list.print_linked_list()