import codecs
import nltk
import csv 
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


# Read data
csvFile = open('PTP Project\Data\G20Indonesia_Preprocessing.csv', 'a')
csvWriter = csv.writer(csvFile)

#Stop words present in the library
stopwords = set(nltk.corpus.stopwords.words('indonesian'))

factory = StemmerFactory()
stemmer = factory.create_stemmer()


def remove_stopwords(text):
    output= [i for i in text if i not in stopwords]
    return output

 
with codecs.open('PTP Project\Data\G20Indonesia_Normalization.csv', 'r',"utf-8") as f:
    for line in f:
        print(line)
                
        # Case Folding
        lowerData = []
        for word in line:
            lowerData.append(word.lower())
        
        # Tokenizing
        tokenData = nltk.word_tokenize(lowerData)

        # Filtering
        filteredData = []
        for w in tokenData:
            if w not in stopwords:
                filteredData.append(w)

        # Stemming
        stemWord = stemmer.stem(filteredData)
                
        
        csvWriter.writerow(stemWord)
        print(stemWord)
        print('--------------')
        
        

# data.to_csv('6th Meet (Wednesday, March, 16th 2022)\Task\Data\GoTo_tokenize.csv',encoding='utf8', index=False)



