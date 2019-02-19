import pickle, os, time
import intermediate as i, record as r
    
def mergeSort(inputFileName, sortedFileName, newBlockSize = None, file1='f1.bin', file2='f2.bin', file3='f3.bin', file4='f4.bin'):

    '''
    OBJECTIVE : To merge sort the records on the basis of key values.
    INPUT     : None
    RETURN    : None
    '''

    start = time.time()
    
    if newBlockSize is not None: i.changeBlockSize(newBlockSize)
    
    i.createIntermediateFiles(inputFileName,file1,file2)

    blockSize = i.blockSize
    
    # Merge sort.
    while True:
        
        with open(file1,'rb') as f1, open(file2,'rb') as f2, open(file3,'wb') as f3, open(file4,'wb') as f4:
            
            endOfFile1, endOfFile2 = i.getFileEnd(f1), i.getFileEnd(f2)
            
            if f2.tell() == endOfFile2 : break

            pointer1, pointer2, check = 0, 0, blockSize

            flag = True     # True for f3, False for f4
            
            while True:

                file = f3 if flag else f4
                
                if f2.tell() == endOfFile2:        
                    while f1.tell() < endOfFile1:
                        pickle.dump(pickle.load(f1),file)
                    break

                else:
                    try:

                        record1, record2 = pickle.load(f1), pickle.load(f2)

                        if pointer1 < check and pointer2 < check:
                            while True:
                                if i.getRecordKey(record1) < i.getRecordKey(record2):
                                    pickle.dump(record1,file)
                                    pointer1 += 1
                                    if pointer1 < check : record1 = pickle.load(f1)
                                    else: break
                                else:
                                    pickle.dump(record2,file)
                                    pointer2 += 1
                                    if pointer2 < check : record2 = pickle.load(f2)
                                    else: break
                        
                        if pointer1 < check:
                            while True:
                                    pickle.dump(record1,file)
                                    pointer1 += 1
                                    if pointer1 < check : record1 = pickle.load(f1)
                                    else: break
                                    
                        if pointer2 < check:
                            while True:
                                    pickle.dump(record2,file)
                                    pointer2 += 1
                                    if pointer2 < check : record2 = pickle.load(f2)
                                    else: break

                        check += blockSize
                        flag = False if flag else True

                    except:
                        pickle.dump(record1,file)

        os.remove(file1),os.remove(file2)
        os.rename(file3, file1), os.rename(file4,file2)
        blockSize *= 2
        
    if os.path.exists(sortedFileName): os.remove(sortedFileName) 
    os.rename(file1,sortedFileName), os.remove(file2), os.remove(file3), os.remove(file4)

    end = time.time()
    
    return end-start
