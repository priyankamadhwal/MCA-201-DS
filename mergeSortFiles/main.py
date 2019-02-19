import record as r
from mergeSortFiles import mergeSort
#import matplotlib.pyplot as mplot

'''
def plotGraph(fileName):
    
    OBJECTIVE : To plot a graph execution time v/s block size.
    INPUT     : None
    RETURN    : None
 

    file = open('coordinates.bin','wb')
    x = [100,1000,10000,30000,60000,90000,120000,150000,180000,210000,240000,270000]
    y = [mergeSort(fileName,i) for i in x]
    pickle.dump(x,file)
    pickle.dump(y,file)
    file.close()
 
    
    file = open('coordinates.bin','rb')
    x = pickle.load(file)
    y = pickle.load(file)
    file.close()
    mplot.plot(x,y)
    mplot.xlabel('Block-Size')
    mplot.ylabel('Execution Time (sec)')
    mplot.title('Merge Sort Files')

    mplot.show()
'''

def main():
    '''
    OBJECTIVE : Main function.
    INPUT     : None
    RETURN    : None
    '''
    inputFile, sortedFile = input('Enter the name of file whose records you want to sort : '), input('Enter the name of file in which you want to store the sorted records : ')
    totalRecords = 5000000
    r.saveRecords(inputFile, totalRecords)
    print(mergeSort(inputFile, sortedFile, 100))
    #plotGraph(inputFile)
    r.fetchRecords(sortedFile)
    
if __name__ == '__main__':
    main()

