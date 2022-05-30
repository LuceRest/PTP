import codecs
import nltk
import csv 


csvFile = open('6th Meet (Monday, March, 14th 2022)\Practice\Data\GoTo_Case.csv', 'a')
csvWriter = csv.writer(csvFile)

    
with codecs.open('6th Meet (Monday, March, 14th 2022)\Practice\Data\GoTo_Normalization.csv', 'r',"utf-8") as f:
    for line in f:
        # print(line)
        lowerData = line.lower()

        csvWriter.writerow(lowerData)
        print(lowerData)
        print('--------------')
        
        

# data.to_csv('6th Meet (Wednesday, March, 16th 2022)\Task\Data\GoTo_tokenize.csv',encoding='utf8', index=False)



