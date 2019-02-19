import pickle, random

class Record:
    '''
    A class to represent a Record.
    '''
    
    def __init__(self, key, nonKey):
        '''
        OBJECTIVE : To initialize the object of class Record.
        INPUT     :
             self : (Imlicit Parameter) An object of class record.
              key : Integer, the key attribute.
           nonKey : String, the non-key attribute.
        RETURN    : None
        '''
        self.key = key
        self.nonKey = nonKey
        
    def __str__(self): 
        '''
        OBJECTIVE : To return a string representation of an object of the Record class.
        INPUT     :
             self : (Imlicit Parameter) An object of class Record.
        RETURN    : String representation of Record object.
        '''
        return 'KEY : '+str(self.key)+'\tNON_KEY : '+self.nonKey

def saveRecords(fileName, totalRecords):
    '''
    OBJECTIVE : To save records in a file.
    INPUT     : None
    RETURN    : None
    '''

    startKey = 10000001
    minKey, maxKey, constant = startKey, startKey+totalRecords, 5
    allKeys = random.sample(range(minKey, maxKey), totalRecords)
    with open(fileName,'wb') as inputFile:
        for key in allKeys:
            nonKey = str(key)*constant
            pickle.dump(Record(key, nonKey), inputFile)
            
def printAllRecords(fileName):
    '''
    OBJECTIVE : To print all the records in the given file.
    INPUT     :
     fileName : The name of the file.
    RETURN    : None
    '''
    with open(fileName,'rb') as f:
        while True:
            try:
                print(pickle.load(f))
            except:
                break
    print('\n')
                

def fetchRecords(fileName):
    '''
    OBJECTIVE : To fetch and print records within a given range.
    INPUT     : None
    RETURN    : None
    '''
    ans = 'y'
    while ans == 'y':
        print('Enter a range to retrieve records... ')
        start, end = int(input('START ==>> ')), int(input('END ==>> '))
        f = open(fileName,'rb')
        pickle.load(f)
        size = f.tell()
        f.seek(size*(start-1))
        for recordNo in range(start, end+1):
            print(recordNo,'.\t',pickle.load(f),sep='')
        f.close()
        ans = input("\nDo you want to continue? (Enter 'y' or 'Y' for YES and anything else for NO) : \n").lower()
        print('\n')
