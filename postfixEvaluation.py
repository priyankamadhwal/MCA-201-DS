from stack import Stack

def postfixEvaluation(expression):
    '''
    OBJECTIVE       : To evaluate a given postfix expression.
    INPUT           :  
         expression : An expression in postfix notation (operators and operands seperated by a space).
    OUTPUT          : Result after the evaluation of given postfix expression.
    '''
    # APPROACH      : If character is operand, push it onto the stack.
    #                 Else if its an operator, pop two operands from the stack and perform the operation. Then, push the result onto stack.

    s = Stack()
    expression = expression.split()
    for c in expression:
        if c.isdecimal(): s.push(c)
        else:
            op1, op2 = s.pop(), s.pop()
            s.push(str(eval(op2+c+op1)))
        #print('c:',c,'s:',s) 
    return s.pop()
