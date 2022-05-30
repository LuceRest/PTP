import codecs
import nltk
import csv 


csvFile = open('6th Meet (Wednesday, March, 16th 2022)\Task\Data\GoTo_Stemming_w_Tokenize.csv', 'a')
csvWriter = csv.writer(csvFile)

    
with codecs.open('6th Meet (Wednesday, March, 16th 2022)\Task\Data\GoTo_Stemming.csv', 'r',"utf-8") as f:
    for line in f:
        # print(line)
        tokenData = nltk.word_tokenize(line)
        csvWriter.writerow(tokenData)
        print(tokenData)
        print('--------------')
        
        

# data.to_csv('6th Meet (Wednesday, March, 16th 2022)\Task\Data\GoTo_tokenize.csv',encoding='utf8', index=False)



