import pickle, os, time

blockSize = 2

def changeBlockSize(new):
    '''
    OBJECTIVE : To change the blockSize.
    INPUT     :
          new : New blockSize.
    RETURN    : None.
    '''
    global blockSize
    blockSize = new

def getFileEnd(file):
    '''
    OBJECTIVE : To find the end of a file.
    INPUT     :
         file : The file whose end is to be found.
    RETURN    : End of file.
    '''
    endOfFile = file.seek(0,os.SEEK_END)
    file.seek(0)
    return endOfFile

def getRecordKey(record):
    '''
    OBJECTIVE : To return the value of key attribute of the given record.
    INPUT     :
       record : An object of class Record.
    RETURN    : Key value of the given record.
    '''
    return record.key

def createIntermediateFiles(fileName, f1, f2):
    '''
    OBJECTIVE : To create two intermediate files f1 and f2 from an input file.
    INPUT     : None
    RETURN    : None
    '''
    global blockSize

    # Create files f1 and f2.
    with open(fileName,'rb') as inputFile, open(f1,'wb') as f1, open(f2,'wb') as f2:
        endOfFile = getFileEnd(inputFile)
        while inputFile.tell() < endOfFile:
            list1, list2 = [[pickle.load(inputFile) for _ in range(blockSize) if  inputFile.tell() < endOfFile] for _ in range(2)]
            list1.sort(key = getRecordKey)
            list2.sort(key = getRecordKey)
            for x in list1: pickle.dump(x,f1)
            for y in list2: pickle.dump(y,f2)

