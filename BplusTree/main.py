import BPlusTree, record

noOfRecords = 10000

def main():    
    '''
    OBJECTIVE : The main function.
    INPUT: None
    RETURN: None
    '''
    #t = BPlusTree.hardcodedTree()

    record.createDataFile(noOfRecords)
    #record.printFile('dataFile.bin')
    while True:
        try:
            t = BPlusTree.createBPlusTree('dataFile.bin')
            break
        except:
            BPlusTree.updateNodeSpace()
    
    t.printIndexFile()

    while True:
        '''
        try:
            key = int(input('\n\nEnter the key you want to search : '))
        except:
            print('The value of key must be a positive number.')
        ans = t.search(key)
        if ans:
            ans = ans[1]
            print('SUCCESS!!! The given key exists as :',ans)
            print('\nRECORD FROM DATA FILE WITH KEY',key,': ',record.fetchRecord('dataFile.bin',ans[1]))
        else:
            print('FAILURE!!! The given key does not exists.')
        ''' 
        try:
            key = int(input('\n\nEnter a key : '))
        except:
            print('The value of key must be a positive number.')
            continue
        try:
            noOfRec = int(input('Enter no. of keys : '))
        except:
            print('Enter a positive number.')
            continue
        t.printKeysStartingFrom(key,noOfRec)
        
        c = None
        while c not in ['y', 'Y', 'n', 'N']:
            c = input('\nDo you want to continue? (y/n) : ')
        if c in ['n','N']: break

if __name__ == '__main__':
    main()
