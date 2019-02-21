import pickle
import intermediate as i

def binarySearch(file, recordSize, findKey, low, high):

    '''
    OBJECTIVE : To find the given key using binary search.
    INPUT     :
         file : The file in which search is to be performed.
   recordSize : Size of one record.
          key : The key which is to be found.
          low : The low index.
         high : The high index.
    RETURN    : The index of the record, if found. Else, -1.
    '''
    
    if low <= high:

        middle = (low + high) // 2

        file.seek(recordSize * middle)

        currRecordKey = i.getRecordKey(pickle.load(file))

        if currRecordKey == findKey:
            return middle

        elif currRecordKey < findKey:
            return binarySearch(file, recordSize, findKey, middle+1, high)

        else:
            return binarySearch(file, recordSize, findKey, low, middle-1)

    return -1

         
     
