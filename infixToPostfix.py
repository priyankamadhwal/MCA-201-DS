from stack import Stack

def infixToPostfix(infix):

    '''
    OBJECTIVE      : To transform a given expression from infix to postfix.
    INPUT          :  
             infix : Expression in infix notation.
    RETURN         : Expression in postfix notation.
    '''
    # APPROACH     : If a character is operand, append it with the result string. Else, push operator onto stack.
    #                Check precedence of operators.
    #                If precendence of incoming operator is low or equal to the operator at the top of stack then pop that operator, and append to the result string.
    #                Then push the incoming operator onto stack.
    s, postfix = Stack(), ''
    priority = {
                        '(':4,
                        '^':3,
                        '/':2,
                        '*':2,
                        '+':1,
                        '-':1,
                        ')':0
                    }
    for c in infix:

        if c.isalnum(): postfix += c         
        else:                                
            if s.isEmpty(): s.push(c)
            elif priority[c] > priority[s.peek()] : s.push(c)
            else:
                while not s.isEmpty() and priority[c] <= priority[s.peek()]:
                    if s.peek() != '(':
                        postfix += s.pop()
                    elif c == ')':
                        while s.peek() != '(':
                            postfix += s.pop()
                        s.pop()
                        break
                    else: break
                if c!= ')':
                    s.push(c)
        #print('Postfix:',postfix,'Stack:',s)
    while not s.isEmpty(): postfix += s.pop()

    return postfix
