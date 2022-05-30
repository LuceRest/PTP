import codecs
import nltk
import csv 


csvFile = open('6th Meet (Wednesday, March, 16th 2022)\Task\Data\GoTo_Filtering.csv', 'a')
csvWriter = csv.writer(csvFile)

#Stop words present in the library
stopwords = set(nltk.corpus.stopwords.words('indonesian'))

def remove_stopwords(text):
    output= [i for i in text if i not in stopwords]
    return output
    
with codecs.open('6th Meet (Wednesday, March, 16th 2022)\Task\Data\GoTo_Case_Folding.csv', 'r',"utf-8") as f:
    for line in f:
        # print(line)
        tokenData = nltk.word_tokenize(line)
        # print(tokenData)

        filteredData = []

        for w in tokenData:
            if w not in stopwords:
                filteredData.append(w)
        
        csvWriter.writerow(filteredData)
        print(filteredData)
        print('--------------')
        
        

# data.to_csv('6th Meet (Wednesday, March, 16th 2022)\Task\Data\GoTo_tokenize.csv',encoding='utf8', index=False)



