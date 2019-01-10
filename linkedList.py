class Node:
    '''
    A class to represent a node.
    '''

    def __init__(self, data):
        '''
        OBJECTIVE     : To initialize an object of the class Node.
        INPUT         :
                 self : (Implicit parameter) An object of class Node.
                 data : Data that is to be stored in the node.
        RETURN        : None.
        '''
        # APPROACH    : Store the given data in the node and initially, the next is equal to None.
        self.data = data
        self.next = None

class LinkedList:
    '''
    A class to represent the Linked List.
    '''

    def __init__(self):
        '''
        OBJECTIVE     : To initialize an object of the class LinkedList.
        INPUT         :
                 self : (Implicit parameter) An object of class LinkedList.
        RETURN        : None.
        '''
        # APPROACH    : Initially the linked list is empty, so head = None.
        self.head = None

    def insertBegin(self, data):
        '''
        OBJECTIVE     : To insert a node at the beginning of the linked list.
        INPUT         :
                 self : (Implicit parameter) An object of class LinkedList.
                 data : Data of the node which is to be inserted.
        RETURN        : None.
        '''
        # SIDE EFFECT : Modifies the linked list by inserting a new node at the beginning.
        # APPROACH    : Create a new node. Next of this node will point to head. Then move the head to this new node.
        newNode = Node(data)
        newNode.next, self.head = self.head, newNode

    def deleteBegin(self):
        '''
        OBJECTIVE     : To delete a node from the beginning of the linked list.
        INPUT         :
                 self : (Implicit parameter) An object of class LinkedList.
        RETURN        : A message to indicate whether the node was deleted successfully or not.
        '''
        # SIDE EFFECT : Modifies the linked list by deleting a new node from the beginning.
        # APPROACH    : If linked list is empty, return. Else, move the head to next node and delete previous node.
        if self.head == None :
            return 'Linked list is empty!'
        temp, data, self.head = self.head, self.head.data, self.head.next
        del temp
        return 'Node with data '+str(data)+' successfully deleted from the beginning of the linked list!'

    def insertSortedList(self, data, current=None, prev=None):
        '''
        OBJECTIVE     : To insert a node such that the linked list remains sorted.
        INPUT         :
                 self : (Implicit parameter) An object of class LinkedList.
                 data : Data of the node which is to be inserted.
              current : Current node, whose value is compared with the given data.
                 prev : Previous node, prev.next is current.
        RETURN        : None.
        '''
        # SIDE EFFECT : Modifies the linked list by inserting a new node such that the list remains sorted.
        # APPROACH    : RECURSIVE
        #               Initially, current is self.head and prev is None.
        #               If linked list is empty, then create a new Node. Point the head to this new node.
        #               Else if end of the linked list is reached, i.e. current is None, then create a  new node and link it to prev.next.
        #               Else if current.data is greater or equal to the given data, then insert a new node between prev and current.
        #                                                                           If current is self.head, then move head to the new node.
        #               Else call self.insertSortedList(data, current.next, current).
        
        if current is None and prev is None:        # Initially
            current = self.head
            
        if self.head is None:                       # Linked list is empty
            self.head = Node(data)
        elif current is None:                       # End of the list
            prev.next = Node(data)
        elif current.data >= data:
            newNode = Node(data)
            if current == self.head:
                newNode.next, self.head = self.head, newNode
            else:
                prev.next, newNode.next = newNode, current
        else:
            return self.insertSortedList(data, current.next, current)
            
                
    def deleteNode(self, data):
        '''
        OBJECTIVE     : To delete a node with given data.
        INPUT         :
                 self : (Implicit parameter) An object of class LinkedList.
                 data : Data in the node which is to be deleted.
        RETURN        : A message to indicate whether the node was deleted successfully or not.
        '''
        # SIDE EFFECT : Modifies the linked list by deleting a node with given data.
        # APPROACH    : Search the node to be deleted, and then use del operator to delete the node after modifying the links.
        
        if self.head == None :                       # Linked list is empty.
            return 'Linked list is empty!'

        current, prev = self.head, None
        while current is not None and current.data != data:
            prev, current = current, current.next
        if current == None:
            return 'Node with data '+str(data)+' does not exist in the linked list!'
        if current == self.head :
            self.head = self.head.next
        else:
            prev.next = current.next
        del current
        return 'Node with data '+str(data)+' deleted successfully from the linked list!'

    def deleteNodeRec(self, data, current=None, prev=None):
        '''
        OBJECTIVE     : To delete a node with given data.
        INPUT         :
                 self : (Implicit parameter) An object of class LinkedList.
                 data : Data of the node which is to be deleted.
              current : Current node, whose value is compared with the given data.
                 prev : Previous node, prev.next is current.
        RETURN        : A message to indicate whether the node was deleted successfully or not.
        '''
        # SIDE EFFECT : Modifies the linked list by deleting a node with given data.
        # APPROACH    : RECURSEIVE
        #               Initially, current is self.head and prev is None.
        #               If linked list is empty, then return.
        #               Else if current is None, node was not found, return.
        #               Else if current.data is equal to given data, the delete node and return
        #               Else call self.deleteNodeRec(data, current.next, current)
        
        if current is None and prev is None:        # Initially    
            current = self.head

        if self.head == None:                       # Linked list is empty
            return 'Linked list is empty!'
        elif current == None:                       # Node not found
            return 'Node with data '+str(data)+' does not exist in the linked list!'
        elif current.data == data:                  # Node found
            if current == self.head:
                self.head = current.next
            else:
                prev.next = current.next
            del current
            return 'Node with data '+str(data)+' deleted successfully from the linked list!'
        else:
            return self.deleteNodeRec(data, current.next, current)

    def __str__(self):
        '''
        OBJECTIVE     : To return the string representation of an object of LinkedList class.
        INPUT         :
                 self : (Implicit parameter) An object of class LinkedList.
        Return        : A string representation of given object.
        '''
        # APPROACH    : Concatenate the node values, starting from head till last node.
        if self.head == None : return 'Empty!'
        
        string = ''
        current = self.head
        while current.next != None:
            string += str(current.data)+' -> '
            current = current.next
        string += str(current.data)
        return string

def main():
    '''
    OBJECTIVE : Display a menu to user to perform operations a Linked List.
    INPUT     : None
    OUTPUT    : None
    '''

    print('************************** LINKED LIST MENU **************************')
    print(' 1. INSERT AT BEGINNING \n 2. INSERT IN SORTED ORDER \n 3. DELETE FROM BEGINNING \n 4. DELETE A NODE \n 5. DISPLAY \n 6. EXIT')
    print('**********************************************************************')
    print()
        
    newLL = LinkedList()
    
    while True:
        
        choice = input('Enter your choice (1/2/3/4/5/6) ==>> : ')
        
        if choice == '1'   : newLL.insertBegin(input('Enter data ==>> '))
        elif choice == '2' : newLL.insertSortedList(input('Enter data ==>> '))
        elif choice == '3' : print(newLL.deleteBegin())
        elif choice == '4' : print(newLL.deleteNodeRec(input('Enter data of the node to be deleted ==>> ')))
        elif choice == '5' : print(newLL)
        elif choice == '6' : break
        else : print('ERROR!!! Wrong choice.')
        
        print('\n')

if __name__ == '__main__':
    main()
