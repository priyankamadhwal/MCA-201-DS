import numpy

maxKeys = 50
empty = numpy.int64(999999)
NONE = numpy.int64(-1)
TRUE = numpy.int64(1)
FALSE = numpy.int64(0)

class Node:
    '''
    A node for the index file.
    '''
    def __init__(self, isLeaf = TRUE):
        '''
        OBJECTIVE : To initialize an object of class Node.
        INPUT :
            self   : Implicit parameter, object of class Node.
            isLeaf : True if the given node is a leaf, else false.
        RETURN : None
        '''
        self.keys = [(empty,empty)]*maxKeys
        self.links = [empty]*(maxKeys+1)
        self.parent = NONE
        self.currKeysIndex = numpy.int64(0)
        self.currLinksIndex = numpy.int64(0)
        self.isLeaf = isLeaf

    def add(self, keyTup):
        '''
        OBJECTIVE : To add a key-index tuple in given node.
        INPUT :
            self : Implicit parameter, object of class Node.
            keyTup : Key-index tuple.
        RETURN : None
        '''
        self.keys[self.currKeysIndex] = keyTup
        self.currKeysIndex += 1
        self.keys.sort(key = getKey)

    def split(self, keyTup=None):
        '''
        OBJECTIVE : Split the node into two and return the middle key-index tuple and the new node.
        INPUT :
            self : Implicit parameter, object of class Node.
            keyTup : Key-index tuple.
        RETURN : middle key-index tuple, new node
        '''
        temp = sorted(self.keys + ([keyTup] if keyTup else []), key = getKey)
        mid = maxKeys//2
        self.keys = temp[:mid] + [(empty,empty)]*(maxKeys-mid)
        self.currKeysIndex = mid
        isLeaf = self.isLeaf
        newNode = Node(isLeaf)
        newNode.keys = (temp[mid:] if isLeaf==TRUE else temp[mid+1:]) + [(empty,empty)]*((maxKeys-mid-1) if keyTup else (maxKeys-mid))
        newNode.currKeysIndex = maxKeys-mid+1 if keyTup else (maxKeys-mid)
        return temp[mid], newNode

    def __str__(self):
        '''
        OBJECTIVE : To return a string representation of the object of a Node class.
        INPUT :
            self : Implicit parameter, object of class Node.
        RETURN : String representation of the given node.
        '''
        return str(self.keys) + ' :: ' + str(self.links)

def newNode():
    '''
    OBJECTIVE : Return a new Node object.
    INPUT: None
    RETURN : None 
    '''
    return Node()
    

def getKey(tup):
    '''
    OBJECTIVE : Return the key from the given tuple.
    INPUT:
        tup : Tuple from which key is to be retrieved.
    RETURN : Key 
    '''
    return tup[0]
