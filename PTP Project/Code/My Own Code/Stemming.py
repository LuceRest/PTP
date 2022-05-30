import codecs
import nltk
import csv 
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# from Sastrawi.Stemmer import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

csvFile = open('PTP Project\Data\G20Indonesia_Stemming.csv', 'a')
csvWriter = csv.writer(csvFile)

    
with codecs.open('PTP Project\Data\G20Indonesia_Filtering.csv', 'r',"utf-8") as f:
    for line in f:
        # print(line)
        # tokenData = nltk.word_tokenize(line)
        stemWord = stemmer.stem(line)
        csvWriter.writerow(stemWord)
        print(stemWord)
        print('--------------')
        
        

# data.to_csv('6th Meet (Wednesday, March, 16th 2022)\Task\Data\GoTo_tokenize.csv',encoding='utf8', index=False)



