class Stack:
    '''
    Creating a Stack class and performing stack operations.
    '''
    def __init__(self):
        '''
        OBJECTIVE     : Initializing a stack.
        INPUT         :
                 self : Implicit parameter, an object of Stack class.
        RETURN        : None
        '''
	# SIDE EFFECT : None
	# APPROACH    : Create an empty stack list.
        self.stack = []
		
    def isEmpty(self):
        '''
        OBJECTIVE     : To check whether the stack is empty or not.
        INPUT         :
                 self : Implicit parameter, an object of Stack class.
        RETURN        : True if stack is empty, else False.
        '''
	# SIDE EFFECT : None
        # APPROACH    : Check if the stack is equal to [].
        return self.stack == []
        
    def push(self,element):
        '''
        OBJECTIVE 	  : To push an element on the top of stack.
        INPUT         :
                 self : Implicit parameter, an object of Stack class.
              element : Integer, the element which is to be pushed onto stack.
        RETURN        : None
        '''
	# SIDE EFFECT : Modifies the stack by adding an element at the top.
        # APPROACH    : Use append() function.
        self.stack.append(element)

    def pop(self):
        '''
        OBJECTIVE     : To remove an element from the top of stack.
        INPUT         :
                 self : Implicit parameter, an object of Stack class.
        RETURN        : Top element of stack.
        '''
      	# SIDE EFFECT : Modifies the stack by removing an element from the top.
        # APPROACH    : Use pop() function.
        return self.stack.pop()

    def peek(self):
        '''
        OBJECTIVE     : To find the top element of stack.
        INPUT         :
                 self : Implicit parameter, an object of Stack class.
        RETURN        : Top element of stack.
        '''
      	# SIDE EFFECT : None.
        # APPROACH    : Return last element (at index -1) if stack is not empty, else return None.
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None

    def __str__(self):
        
        '''
        OBJECTIVE     : To create and return the string representation of an object of Stack class.
        INPUT         :
                 self : Implicit parameter, an object of Stack class.
        RETURN        : None
        '''
        # SIDE EFFECT : None.
        # APPROACH    : Use join() function on stack list.
        return '[ '+', '.join(self.stack)+' ]'

def main():
    
    '''
    OBJECTIVE : Display a menu to user to perform stack operations.
    INPUT     : None
    OUTPUT    : None
    '''

    print('************************** STACK MENU **************************')
    print(' 1. PUSH \n 2. POP \n 3. DISPLAY \n 4. EXIT')
    print('****************************************************************')
    print()
        
    s = Stack()
    
    while True:
        
        choice = input('Enter your choice (1,2,3,4) ==>> : ')
        
        if choice == '1'   : s.push(input('Enter element ==>> '))
        elif choice == '2' : print('Element popped ==>> '+str(s.pop()) if not s.isEmpty() else 'Underflow error!!! Stack is empty.')
        elif choice == '3' : print(s)
        elif choice == '4' : break
        else : print('ERROR!!! Wrong choice.')
        
        print('\n')

if __name__ == '__main__':
    main()
