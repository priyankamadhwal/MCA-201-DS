import os, numpy, pickle, record, node as n

nodeSpace = 4500
maxKeys = n.maxKeys
empty = n.empty
NONE = numpy.int64(-1)
TRUE = numpy.int64(1)
FALSE = numpy.int64(0)

class BPlusTree:
    '''
    A class that represents B+ tree data structure.
    '''

    def __init__(self, indexFileName='indexFile.bin'):
        '''
        OBJECTIVE : To initialize an object of class BPlusTree.
        INPUT :
            self : Implicit parameter, object of class BPlusTree.
        RETURN : None
        '''
        self.indexFile = indexFileName
        self.indexPosFile = 'pos'+self.indexFile[:1].upper()+self.indexFile[1:]
        if os.path.exists(self.indexFile): os.remove(self.indexFile)
        if os.path.exists(self.indexPosFile): os.remove(self.indexPosFile)
        rootInfo = n.Node()
        rootInfo.keys[0] = (numpy.int64(1), empty)
        root = n.Node()
        self.appendInIndexFile(rootInfo)
        self.appendInIndexFile(root)

    def findNodeIndexToInsert(self,key):
        '''
        OBJECTIVE : To find the index of the node in index file to insert the given key in B+ tree.
        INPUT :
            self : Implicit parameter, object of class BPlusTree.
            key : Key to be inserted.
        RETURN : The index of node in which the given key is to be inserted.
        '''
        rootIndex = self.getNodeFromIndexFile(0).keys[0][0]
        currentIndex, current = rootIndex, self.getNodeFromIndexFile(rootIndex)
        while current.isLeaf == FALSE:
            i = 0
            while True:
                if i == maxKeys or current.keys[i][0] == empty or current.keys[i][0] > key: break
                i += 1
            currentIndex, current = current.links[i], self.getNodeFromIndexFile(current.links[i])
        return currentIndex            

    def insert(self, keyTup):
        '''
        OBJECTIVE : To add a given key-index tuple in given node.
        INPUT :
            self : Implicit parameter, object of class BPlusTree.
            keyTup : Key-Index tuple.
        RETURN : None
        '''
        nodeIndex = self.findNodeIndexToInsert(n.getKey(keyTup))
        node = self.getNodeFromIndexFile(nodeIndex)
        try:
            node.add(keyTup)
            self.updateNodeInIndexFile(node,nodeIndex)
        except:
            self.balance(nodeIndex,keyTup)

    def balance(self, splitNodeIndex, keyTup=None):
        '''
        OBJECTIVE : To perform splitting and balance operation on the node of the given B+ tree.
        INPUT :
            self : Implicit parameter, object of class BPlusTree.
            splitNodeIndex : Index of the node which is to be splitted.
            keyTup : Key-Index tuple.
        RETURN : None
        '''
        splitNode = self.getNodeFromIndexFile(splitNodeIndex)
        midKeyTup, newNode = splitNode.split(keyTup)
        indexPosList=[]
        with open(self.indexPosFile,'rb') as indexPosFile:
            indexPosList = pickle.load(indexPosFile)
        self.appendInIndexFile(newNode)
        newNodeIndex = numpy.int64(len(indexPosList))
        parentNode, parentNodeIndex = NONE, NONE
        if splitNode.parent == NONE:
            parentNode, parentNodeIndex = n.Node(FALSE), numpy.int64(len(indexPosList)+1)
            self.appendInIndexFile(parentNode)
            rootInfo = self.getNodeFromIndexFile(0)
            rootInfo.keys[0] = (parentNodeIndex,empty)
            self.updateNodeInIndexFile(rootInfo,0)
            splitNode.parent = parentNodeIndex
            parentNode.links[parentNode.currLinksIndex] = splitNodeIndex
            parentNode.currLinksIndex += 1
        else:
            parentNode, parentNodeIndex = self.getNodeFromIndexFile(splitNode.parent), splitNode.parent
        newNode.parent = parentNodeIndex
        parentNode.keys = sorted(parentNode.keys[:parentNode.currKeysIndex]+[midKeyTup]+[(empty,empty)]*(maxKeys-parentNode.currKeysIndex-1),key=n.getKey)
        parentNode.currKeysIndex += 1
        keysTemp = [n.getKey(x) for x in parentNode.keys]
        i = keysTemp.index(n.getKey(midKeyTup))
        parentNode.links = parentNode.links[:i+1] + [newNodeIndex] + parentNode.links[i+1:parentNode.currLinksIndex] +[empty]*(maxKeys - parentNode.currLinksIndex)
        parentNode.currLinksIndex += 1
        if splitNode.isLeaf == TRUE:
            if splitNode.currKeysIndex != 0:
                newNode.links[0] = splitNode.links[0]
            splitNode.links[0] = newNodeIndex
        else:
            mid = maxKeys//2
            newNode.links = splitNode.links[mid+1:maxKeys+2] + [empty]*(maxKeys-mid)
            splitNode.links = splitNode.links[:mid+1] + [empty]*(maxKeys-mid)
            splitNode.currLinksIndex = numpy.int64(maxKeys//2 + 1)
            newNode.currLinksIndex = numpy.int64(maxKeys+2 - splitNode.currLinksIndex)
            for link in splitNode.links:
                if link == empty: break
                currNode = self.getNodeFromIndexFile(link)
                currNode.parent = splitNodeIndex
                self.updateNodeInIndexFile(currNode,link)
            for link in newNode.links:
                if link == empty: break
                currNode = self.getNodeFromIndexFile(link)
                currNode.parent = newNodeIndex
                self.updateNodeInIndexFile(currNode,link)
        self.updateNodeInIndexFile(splitNode,splitNodeIndex)
        self.updateNodeInIndexFile(newNode,newNodeIndex)
        self.updateNodeInIndexFile(parentNode,parentNodeIndex)

        if len(parentNode.keys) > maxKeys and len(parentNode.links) > maxKeys+1: self.balance(parentNodeIndex)
        

    def search(self,key):
        '''
        OBJECTIVE : To search the given key in the B+ tree.
        INPUT :
            self : Implicit parameter, object of class BPlusTree.
            key  : The key to be searched.
        RETURN : If the key exists, return the key-index tuple. Else, return None.
        '''
        with open(self.indexFile,'rb') as f:
            rootIndex = pickle.load(f).keys[0][0]
            current = self.getNodeFromIndexFile(rootIndex)
            while not current.isLeaf:
                i = 0
                while True:
                    if i == maxKeys or current.keys[i][0] == empty or current.keys[i][0] > key: break
                    i += 1
                current = self.getNodeFromIndexFile(current.links[i])
            currentKeys = [n.getKey(x) for x in current.keys]
            if key in currentKeys:
                return current, current.keys[currentKeys.index(key)]
            else:
               return None

    def printKeysStartingFrom(self,key,noOfKeys=None):
        '''
        OBJECTIVE : To print all the keys starting from the given key in the B+ tree.
        INPUT :
            self : Implicit parameter, object of class BPlusTree.
            key  : The key to be searched.
        RETURN : If the key exists, return the key-index tuple. Else, return None.
        '''
        current = self.search(key)
        if not current:
            print('FAILURE!!! The key',key,'does not exists in the given B+ tree.')
            return
        current = current[0]
        currentKeys = [n.getKey(x) for x in current.keys]
        if not noOfKeys: noOfKeys = noOfRecords
        keyIndex = currentKeys.index(key)
        i = 0
        while i < noOfKeys:
            try:
                if keyIndex == current.currKeysIndex:
                    keyIndex = 0
                    current = self.getNodeFromIndexFile(current.links[0])
                print(record.fetchRecord('dataFile.bin',current.keys[keyIndex][1]))
                i += 1
                keyIndex += 1
            except: break
        if i < noOfKeys: print("\nCan't find more nodes!!!")

    def printIndexFile(self):
        '''
        OBJECTIVE : To print the index file of the given B+ tree.
        INPUT :
            self : Implicit parameter, object of class BPlusTree.
        RETURN : None
        '''
        print('FINAL INDEX FILE:\n')
        loc = 0
        with open(self.indexFile,'rb') as indexFile:
            while True:
                try:
                    indexFile.seek(loc)
                    obj = pickle.load(indexFile)
                    print(obj)
                    loc += nodeSpace
                except EOFError: break

    def getNodeFromIndexFile(self, loc):
        '''
        OBJECTIVE : To retrieve the node from given location.
        INPUT :
            self : Implicit parameter, object of class BPlusTree.
            loc  : Location in index file from which the node is to be retrieved.
        RETURN : None
        '''
        indexPosList = []
        with open(self.indexPosFile,'rb') as f:
            indexPosList = pickle.load(f)
        with open(self.indexFile,'rb') as f:
            f.seek(indexPosList[loc])
            return(pickle.load(f))

    def updateNodeInIndexFile(self, node, loc):
        '''
        OBJECTIVE : To update a node in the index file at given location.
        INPUT :
            self : Implicit parameter, object of class BPlusTree.
            node : The updated node.
            loc  : Location of the node in index file which is to be updated.
        RETURN : None
        '''
        with open(self.indexFile,'r+b') as indexFile, open(self.indexPosFile,'rb') as indexPosFile:
            indexPosList = pickle.load(indexPosFile)   
            indexFile.seek(indexPosList[loc])
            pickle.dump(node,indexFile)

    def appendInIndexFile(self, node):
        '''
        OBJECTIVE : To append a given node at the end of the index file.
        INPUT :
            self : Implicit parameter, object of class BPlusTree.
            node : The node to be appended.
        RETURN : None
        '''
        try:
            with open(self.indexFile,'r+b') as indexFile, open(self.indexPosFile,'r+b') as indexPosFile:
                indexPosList = pickle.load(indexPosFile)
                loc1 = indexPosList[-1] + nodeSpace
                indexPosList.append(loc1)
                indexFile.seek(loc1)
                pickle.dump(node,indexFile)
                loc2 = indexFile.tell()
                #print(loc2-loc1)
                indexPosFile.seek(0)
                pickle.dump(indexPosList,indexPosFile)
        except:
            with open(self.indexFile,'wb') as indexFile, open(self.indexPosFile,'wb') as indexPosFile:
                pickle.dump(node,indexFile)
                pickle.dump([0],indexPosFile)
                #print(indexFile.tell())

def updateNodeSpace():
        '''
        OBJECTIVE : To update the global variable nodeSpace.
        INPUT :
            self : Implicit parameter, object of class BPlusTree.
            node : The node to be appended.
        RETURN : None
        '''
        global nodeSpace
        nodeSpace += 300


def hardcodedTree():
    '''
    OBJECTIVE : To create a hardcoded B+ tree.
    INPUT  : None
    RETURN : None
    '''
    
    # DATAFILE:
    '''
    40 10 60 5 9 86 29 12 55 36 44 24 8 4 90 34 74 22 26 28 50 92 88 96 98 99 105
    '''
    t = BPlusTree()
    
    #Insert 40
    t.insert((40,0))
    
    #Insert 10
    t.insert((10,1))
    
    #Insert 60
    t.insert((60,2))
    
    #Insert 5
    t.insert((5,3))
    
    #Insert 9
    t.insert((9,4))
    
    #Insert 86
    t.insert((86,5))
    
    #Insert 29
    t.insert((29,6))
    
    #Insert 12
    t.insert((12,7))
    
    #Insert 55
    t.insert((55,8))
    
    #Insert 36
    t.insert((36,9))
    
    #Insert 44
    t.insert((44,10))
    
    #Insert 24
    t.insert((24,11))
    
    #Insert 8
    t.insert((8,12))
    
    #Insert 4
    t.insert((4,13))
    
    #Insert 90
    t.insert((90,14))
    
    #Insert 34
    t.insert((34,15))
    
    #Insert 74
    t.insert((74,16))
    
    #Insert 22
    t.insert((22,17))
    
    #Insert 26
    t.insert((26,18))
    
    #Insert 28
    t.insert((28,19))
    
    #Insert 50
    t.insert((50,20))
    
    #Insert 92
    t.insert((92,21))
    
    #Insert 88
    t.insert((88,22))
    
    #Insert 96
    t.insert((96,23))
    
    #Insert 98
    t.insert((98,24))
    
    #Insert 99
    t.insert((99,25))
    
    #Insert 105
    t.insert((105,26))
    
    return t

def createBPlusTree(fileName):
    '''
    OBJECTIVE : To create a B plus tree from the given data file.
    INPUT:
        fileName : Name of the data file from which the B plus tree is to be created.
    RETURN: None
    '''
    t = BPlusTree()
    i = 0
    with open(fileName,'rb') as file:
        while True:
            try:
                key =  record.getRecordKey(pickle.load(file))
                t.insert((key,i))
                i += 1
            except EOFError:
                break
    return t

