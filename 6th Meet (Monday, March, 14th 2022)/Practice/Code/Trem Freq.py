import codecs
import nltk
import csv 


csvFile = open('6th Meet (Wednesday, March, 16th 2022)\Task\Data\GoTo_Trem Freq.csv', 'a')
csvWriter = csv.writer(csvFile)

    
with codecs.open('6th Meet (Wednesday, March, 16th 2022)\Task\Data\GoTo_Stemming.csv', 'r',"utf-8") as f:
    for line in f:
        # print(line)
        word = nltk.word_tokenize(line)
        wordFreq = nltk.FreqDist(word)
        # print(wordFreq)
        # print('-------------------------\n')
        
        csvWriter.writerow(wordFreq.most_common(100))
        print(wordFreq.most_common(100))
        print('-------------------------\n')
        
        
        

# data.to_csv('6th Meet (Wednesday, March, 16th 2022)\Task\Data\GoTo_tokenize.csv',encoding='utf8', index=False)



