import csv
def read_csv_file (csv_file, gender, college, degree):
    file = open(csv_file,'r')
    csvreader = csv.reader(file)
    outlist =[]
    for row in csvreader:
        outlist.append(row)
    result=[]
    for i in outlist:
         if gender in i and college in i and degree in i:
            result.append(i)
    return len(result)

x= read_csv_file('D:\\lab7_files\\Test_Excel.csv','أنثى','الحقوق والعلوم السياسية','البكالوريوس')
print('Total Number Of Students In By Your Choose: ' + str(x))
