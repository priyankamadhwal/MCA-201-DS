import pickle, sys, random

class Record:
    '''
    A class to represent a Record.
    '''
    def __init__(self, key, other):
        '''
        OBJECTIVE : To initialize the object of class Record.
        INPUT     :
             self : (Imlicit Parameter) An object of class Record.
             key  : Integer, record key.
             other: String, record information.
        RETURN    : None
        '''
        #APPROACH : Initialize the given object with given key and other values.
        self.key = key
        self.other = other
    def __str__(self):
        '''
        OBJECTIVE : To return a string representation of an object of the Record class.
        INPUT     :
             self : (Imlicit Parameter) An object of class Record.
        RETURN    : String representation of Record object.
        '''
        #APPROACH : Concatenate strings - str(self.key) and self.other.
        return 'KEY : '+str(self.key) + '\nOTHER : ' + self.other

class Index:
    '''
    A class to represent an Index.
    '''
    def __init__(self, index, key, location):
        '''
        OBJECTIVE : To initialize the object of class Index.
        INPUT     :
             self : (Imlicit Parameter) An object of class Index.
             index: Integer, index number.
               key: Integer, key of the record corresponding to given index.
          location: Integer, location of the record corresponding to given index.
        RETURN    : String representation of Index object self.
        '''
        #APPROACH : Initialize the given object with given index, key and location values.
        self.index = index
        self.key = key
        self.location = location
    def __str__(self):
        '''
        OBJECTIVE : To return a string representation of an object of the Index class.
        INPUT     :
             self : (Imlicit Parameter) An object of class Index.
        RETURN    : None
        '''
        #APPROACH : Concatenate strings - str(self.index), str(self.key) and str(self.location).
        return 'INDEX : '+str(self.index)+'\nKEY : '+str(self.key)+'\nLOCATION : '+str(self.location)

def saveRecords():
    '''
    OBJECTIVE : To save 1,00,00,000 records in a file and create an index file.
    INPUT     : None
    RETURN    : None
    '''
    #APPROACH : Create a Record object comprising: 
    #                  key in the range: 10000001 - 20000001
    #                  other = str(key)*r : r is randomly generated number in the range(minSize, maxSize) = (50, 250)
    #           Make use of seek and tell functions to do the following: 
    #                  Create a file 1 of 1,00,00,000 records.
    #                  Create another 2 file which stores Index object(index, key, location), location refers to the location of record at in file 1.
    minSize, maxSize = 50, 250
    start, end = 10000001, 20000001
    fout1, fout2 = open('Records.bin','wb'), open('Index.bin','wb')
    index = 5000000000
    for i in range(start,end):
        index += 1
        key, other = i, str(i)*random.randint(minSize,maxSize)
        location = fout1.tell()+5000000000
        pickle.dump(Index(index, key, location), fout2)
        pickle.dump(Record(key, other), fout1)
    fout1.close()
    fout2.close()

def fetchRecord(recordNo):
    '''
    OBJECTIVE : To fetch a record (random access) using an index file and print it.
    INPUT     : 
      recordNo: Integer, The record no. which is to be fetched.
    RETURN    : None
    '''
    #APPROACH : Use seek() and tell() functions.
    #           Calculate size of one Index object using tell() function.
    #           Then access the index using seek((recordNo-1)*size) and retrieve the location of the required record.
    fin1, fin2 = open('Records.bin','rb'), open('Index.bin','rb')
    pickle.load(fin2)
    size = fin2.tell()
    fin2.seek((recordNo-1)*size)
    index = pickle.load(fin2)
    print('INDEX FILE\n'+str(index)+'\n')
    location = index.location - 5000000000
    fin1.seek(location)
    record = pickle.load(fin1)
    print('RECORD\n'+str(record)+'\n')
    fin1.close()
    fin2.close()

if __name__ == '__main__':
    saveRecords()
    while True:
        ans = int(input('Which record do you want to retrieve? (Enter non-positive number to exit) ==>> '))
        if ans <= 0: break
        fetchRecord(ans)
