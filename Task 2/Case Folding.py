import codecs
import nltk
import csv 


csvFile = open('Task 2\GoTo_Case Folding.csv', 'a')
csvWriter = csv.writer(csvFile)

    
with codecs.open('Task 2\GoTo_Normalization.csv', 'r',"utf-8") as f:
    for line in f:
        # for word in line:
        # print(line)
        # lowerData = line.lower()
        csvWriter.writerow(line.lower())
        
        print(line)
        print('--------------')
        
        

# data.to_csv('6th Meet (Wednesday, March, 16th 2022)\Task\Data\GoTo_tokenize.csv',encoding='utf8', index=False)



