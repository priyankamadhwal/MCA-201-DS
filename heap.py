class Heap:
    '''
    A class to represent Heap data structure.
    '''
    def __init__(self):
        '''
        OBJECTIVE   : To initialize the heap.
        INPUT       :
               self : (Implicit parameter) An object of heap class.
        RETURN      : None
        '''
        # APPROACH  : Initialize heap with an empty list.

        self.heap = []

    def getParent(self, index):
        '''
        OBJECTIVE   : To find the index of parent of a given node.
        INPUT       :
               self : (Implicit parameter) An object of heap class.
              index : Index of child node.
        RETURN      : Index of parent node.
        '''
        # APPROACH  : Index of parent node is (index-1)//2.
        return (index-1)//2

    def getLeftChild(self, index):
        '''
        OBJECTIVE   : To find the index of left child of a given node.
        INPUT       :
               self : (Implicit parameter) An object of heap class.
              index : Index of parent node.
        RETURN      : Index of left child node.
        '''
        # APPROACH  : Index of left child node is 2*index+1.
        return 2*index+1

    def getRightChild(self, index):
        '''
        OBJECTIVE   : To find the index of right child of a given node.
        INPUT       :
               self : (Implicit parameter) An object of heap class.
              index : Index of parent node.
        RETURN      : Index of right child node.
        '''
        # APPROACH  : Index of right child node is 2*index+2.
        return 2*index+2

    def heapInsert(self, element):
        '''
        OBJECTIVE   : To insert an element in heap.
        INPUT       :
               self : (Implicit parameter) An object of heap class.
            element : The element which is to be inserted.
        RETURN      : None
        '''
        '''
        SIDE EFFECT : Modifies the heap by adding an element.
        '''
        # APPROACH  : Append the element to the heap list, then compare it with its parent. If parent is less than the element, then swap them.
        self.heap.append(element)
        index = len(self.heap)-1
        while index > 0:
            parent = self.getParent(index)
            if self.heap[parent] > element : break
            else : self.heap[index], index = self.heap[parent], parent
        self.heap[index] = element
    
    def heapDeleteMax(self):
        '''
        OBJECTIVE   : To delete an element from the root of the heap.
        INPUT       :
               self : (Implicit parameter) An object of heap class.
        RETURN      : None
        SIDE EFFECT : Modifies the heap by removing an element from the root and changing the positions of some other elements.
        '''
        # APPROACH  : Remove first element, put last element at root and compare it with its children. If element is less than children, then swap. Else, place it there.
        if self.heap != []:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            deletedElement = self.heap.pop()
            if self.heap == []:
                return deletedElement
            value, index = self.heap[0],0
            while index < len(self.heap)-1:
                leftChild, rightChild = self.getLeftChild(index), self.getRightChild(index)
                if leftChild > len(self.heap)-1 : break
                if value >= self.heap[leftChild] and (rightChild > len(self.heap)-1 or value >= self.heap[rightChild]): break
                if (rightChild > len(self.heap)-1) or (self.heap[leftChild] > self.heap[rightChild]):
                    self.heap[index], index = self.heap[leftChild], leftChild
                else:
                    self.heap[index], index = self.heap[rightChild], rightChild
            self.heap[index] = value
            return deletedElement
        else:
            return None

    def buildHeap(self, lst):
        '''
        OBJECTIVE   : To build a heap from a given list.
        INPUT       :
               self : (Implicit parameter) An object of heap class.
                lst : A list from which heap is built.
        RETURN      : None
        '''
        # APPROACH  : Use heapInsert() function on each element of the given list.
        for current in lst:
            self.heapInsert(current)

    def heapSort(self, lst):
        '''
        OBJECTIVE   : To sort a given list in descending order.
        INPUT       :
               self : (Implicit parameter) An object of heap class.
                lst : The list which is to be sorted.
        RETURN      : None
        '''
        # APPROACH  : First build a heap from given list. Then use heapDeleteMax() function to extract the maximum element and append it to the sorted list.
        self.buildHeap(lst)
        sortedList = []
        for i in range(len(self.heap)):
            sortedList.append(self.heapDeleteMax())
        return  sortedList
        
    def __str__(self):
        '''
        OBJECTIVE   : To return a string representation of an object of the Heap class.
        INPUT       :
               self : (Implicit parameter) An object of heap class.
        Return      : None
        '''
        # APPROACH  : Use str() function on heap list.

        return str(self.heap)


    
#16 40 7 16 23 18 12 11 24
h = Heap()
print(h.heapSort([16,40,7,16,23,18,12,11,24]))

