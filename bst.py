class Node:
    '''
    A class to represent a Node of the Binary Search Tree.
    '''
    def __init__(self,data):
        '''
        OBJECTIVE : To initialize an object of class Node.
        INPUT     :
             self :(Implicit parameter) An object of class Node.
             data : The data to be stored at the Node.
        RETURN    : None
        '''
        #APPROACH : Store the given data in the node. The right and left of node is None initially.
        self.data = data
        self.right = None
        self.left = None

class BST:
    '''
    A class to represent a Binary Search Tree.
    '''
    
    def __init__(self):
        '''
        OBJECTIVE : To initialize an object of class BST.
        INPUT     :
             self :(Implicit parameter) An object of class BST.
        RETURN    : None
        '''
        #APPROACH : Root of BST is None initially.
        self.root = None

    def insertInBST(self, data):
        '''
        OBJECTIVE : To insert a node in the binary search tree.
        INPUT     :
             self :(Implicit parameter) An object of class BST.
             data : The data of the node which is to be inserted.
        RETURN    : None
        '''
        #APPROACH : Call insertInBSTHelper().
        self.insertInBSTHelper(data, self.root)

    def insertInBSTHelper(self, data, root):
        '''
        OBJECTIVE : A helper function to insert a node in the binary search tree.
        INPUT     :
             self :(Implicit parameter) An object of class BST.
             data : The data of the node which is to be inserted.
             root : The node which is currently being compared to data.
        RETURN    : None
        '''
        #APPROACH : If root is None, insert at root. Else if data is less than equal to data at root: If left of root is None, insert at root. Else, call this function again on left subtree.
        #           Else if data is more than data at root: If right of root is None, insert at root. Else, call again this function on right subtree.
        if root is None: self.root = Node(data)
        else:
            if data <= root.data:
                if root.left is None:
                    root.left = Node(data)
                else:
                    self.insertInBSTHelper(data, root.left)
            else:
                if root.right is None:
                    root.right = Node(data)
                else:
                    self.insertInBSTHelper(data, root.right)
        

    def inorderTraversal(self):
        '''
        OBJECTIVE : To perform inorder traversal on the Binary Search Tree.
        INPUT     :
             self :(Implicit parameter) An object of class BST.
        RETURN    : None
        '''
        #APPROACH : If root is None, BST is empty, return.
        #           Else call inorderTraversalHelper().
        if self.root is None: return
        self.inorderTraversalHelper(self.root)
        
    def inorderTraversalHelper(self, root):
        '''
        OBJECTIVE : A helper function to perform inorder traversal on the Binary Search Tree.
        INPUT     :
             self :(Implicit parameter) An object of class BST.
             root : The node which is currently being traversed.
        RETURN    : None
        '''
        #APPROACH : If left of root is not None, call inorderTraversalHelper() on left subtree.
        #           Print the data at root.
        #           If right of root is not None, call inorderTraversalHelper() on right subtree.
        if root.left is not None: self.inorderTraversalHelper(root.left)
        print(root.data)
        if root.right is not None: self.inorderTraversalHelper(root.right)
	
    def countNodes(self):
        '''
        OBJECTIVE : To count the number of nodes in the binary search tree..
        INPUT     :
             self :(Implicit parameter) An object of class BST.
        RETURN    : None
        '''
        #APPROACH : Call countNodesHelper().
        return self.countNodesHelper(self.root)
	
    def countNodesHelper(self, root, count=0):
        '''
        OBJECTIVE : A helper function to count the number of nodes in the binary search tree..
        INPUT     :
             self :(Implicit parameter) An object of class BST.
             root : The node which currently being determined.
             count: Current count of nodes.
        RETURN    : None
        '''
        #APPROACH : If root is None, return 0.
        #           Else add count, countNodesHelper() on left subtree, countNodesHelper() on right subtree and 1 for root. Return count. 
        if root is None: return 0
        return count + self.countNodesHelper(root.left) + self.countNodesHelper(root.right) + 1  
        
B = BST()
B.insertInBST(10)
B.insertInBST(9)
B.insertInBST(11)
B.insertInBST(7)
B.insertInBST(8)
B.inorderTraversal()
print(B.countNodes())
