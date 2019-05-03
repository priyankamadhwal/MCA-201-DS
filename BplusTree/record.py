import numpy, pickle, random

class Record:
    '''
    A class to represent the record.
    '''

    def __init__(self,key,nonKey):
        '''
        OBJECTIVE : To inititalize an object of the class Record.
        INPUT :
            key   : The key attribute of the record.
            nonKey: The non-key attribute of the record. 
        '''
        self.key = key
        self.nonKey = nonKey

    def __str__(self):
        '''
        OBJECTIVE : To return a string representation of the object of Record class.
        INPUT :
            self : Implicit parameter, object of class Record.
        RETURN : String representation of the given record.
        '''
        return 'KEY :'+str(self.key) + ' NON-KEY : '+str(self.nonKey)

def getRecordKey(record):
    '''
    OBJECTIVE : To get the key attribute of the given record.
    INPUT :
        record : The record whose key we have to find.

    Return: The key attribute of the given record.
    '''
    return record.key

def createDataFile(noOfRecords):
    '''
    OBJECTIVE : To create a data file of given no. of records.
    INPUT :
        noOfRecords : Number of records.
    RETURN : None
    '''
    with open('dataFile.bin','wb') as dataFile:
        minKey, threshold, mul = 1, 10000000, 1
        allKeys = random.sample(range(minKey,(minKey+noOfRecords)*mul),noOfRecords)
        for key in allKeys:
            key = numpy.int64(key)
            nonKey = str(key+threshold) * 5
            pickle.dump(Record(key,nonKey),dataFile)
    createDataPosFile()

def createDataPosFile():
    '''
    OBJECTIVE : To create a data position file which contains a list of starting positions of all the records in the data file.
    INPUT : None
    RETURN : None
    '''
    dataPosList = []
    with open('dataFile.bin','rb') as dataFile:
        while True:
            dataPosList.append(dataFile.tell())
            try:
                pickle.load(dataFile)
            except:
                break
    with open('posDataFile.bin','wb') as dataFilePos:
        pickle.dump(dataPosList,dataFilePos)

def printFile(fileName):
    '''
    OBJECTIVE : To print the entire given file.
    INPUT :
        filename : Name of the file whose contents are to be printed.
    RETURN : None
    '''
    with open(fileName,'rb') as file:
        while True:
            try:
                print(pickle.load(file))
            except EOFError:
                break

def printFileInRange(fileName, first, last):
    '''
    OBJECTIVE : To print the data in the given file within the given range.
    INPUT :
        filename : Name of the file whose contents are to be printed.
        first : First record no.
        last  : Last record no.
    RETURN : None
    '''
    with open(fileName,'rb') as file:
        pickle.load(file)
        size = file.tell()
        file.seek(size * (first-1))
        while first<=last:
            try:
                print(pickle.load(file))
                first += 1
            except EOFError:
                break

def fetchRecord(fileName,index):
    '''
    OBJECTIVE : To fetch a record from the given location.
    INPUT :
        filename : Name of the file from which record is to be fetched..
        location : The index of the record in given file.
    RETURN : None
    '''
    dataPosList = []
    with open('posDataFile.bin','rb') as dataPosFile:
        dataPosList = pickle.load(dataPosFile)
    with open('dataFile.bin','rb') as dataFile:
        dataFile.seek(dataPosList[index])
        return pickle.load(dataFile)
    

    
            
        
        
