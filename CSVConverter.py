import csv
from ingredientList import ingredientList
def CSVConverter(File):
    '''Assumes File to be a readable File object 
    Writes a "data.csv" file using the DictWriter Format'''
    File.seek(0,0)
    fieldnames = ingredientList(File)
    fieldnames.insert(0,'index')
    with open('data.csv','w',newline='') as dataFile:
        csvFile = csv.DictWriter(dataFile,fieldnames=fieldnames)
        csvFile.writeheader()
        #temp = {i:0 for i in fieldnames}
        File.seek(0)
        lines = File.readlines()
        index = 0
        for line in lines[1:]:
            temp = {i:0 for i in fieldnames}
            temp['index']=index
            arr = line.split()
            for t in arr[1:]:
                temp[t]+=1
            csvFile.writerow(temp)
            index+=1


if( __name__ == "__main__" ):
    with open('a_example',newline='') as File:
        CSVConverter(File)