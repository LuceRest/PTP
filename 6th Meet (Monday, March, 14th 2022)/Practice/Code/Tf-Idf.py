import codecs
import nltk
import csv 
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# from Sastrawi.Stemmer import StemmerFactory
import pandas as pd 
import numpy as np
import ast
import math 


factory = StemmerFactory()
stemmer = factory.create_stemmer()

pathCsvFiltering = '6th Meet (Monday, March, 14th 2022)\Practice\Data\GoTo_Filtering.csv'

# pathCsvTf = '6th Meet (Monday, March, 14th 2022)\Practice\Data\GoTo_Tf.csv'
# pathCsvLf = '6th Meet (Monday, March, 14th 2022)\Practice\Data\GoTo_Lf.csv'
# pathCsvDf = '6th Meet (Monday, March, 14th 2022)\Practice\Data\GoTo_Df.csv'
# pathCsvIdf = '6th Meet (Monday, March, 14th 2022)\Practice\Data\GoTo_Idf.csv'

pathCsvTfIdf = '6th Meet (Monday, March, 14th 2022)\Practice\Data\GoTo_Tf-Idf.csv'


# csvFileTf = open(pathCsvTf, 'a')
# csvFileLf = open(pathCsvLf, 'a')
# csvFileDf = open(pathCsvDf, 'a')
# csvFileIdf = open(pathCsvIdf, 'a')
csvFileTfIdf = open(pathCsvTfIdf, 'a')

# csvWriterTf = csv.writer(csvFileTf)
# csvWriterLf = csv.writer(csvFileLf)
# csvWriterDf = csv.writer(csvFileDf)
# csvWriterIdf = csv.writer(csvFileIdf)
csvWriterTfIdf = csv.writer(csvFileTfIdf)


def convert_text_list(texts):
    texts = ast.literal_eval(texts)
    return [text for text in texts]        


def calc_TF(document):
    #perhitungan jumlah kata
    TF_dict = {}
    for term in document:
        if term in TF_dict:
            TF_dict[term] += 1
        else:
            TF_dict[term] = 1
    #perhitungan tf
    # for term in TF_dict:
    #     TF_dict[term] = TF_dict[term] / len(document)
    return TF_dict

def calc_logFreq(TF):
    logFreq_Dict = {}
    for term in TF:
        if TF[term] > 0:
            logFreq_Dict[term] = 1 + math.log10(TF[term])
        else:
            logFreq_Dict[term] = 0
    return logFreq_Dict

    
def calc_DF(tfDict):
    count_DF = {}
    for term in tfDict:
        # for term in document:
        if term in count_DF:
            count_DF[term] += 1
        else:
            count_DF[term] = 1
    return count_DF

#menghitung idf
# n_document = len(dm)
def calc_IDF(n_document, DF):
    IDF_Dict = {}
    for term in DF:
        IDF_Dict[term] = math.log10(n_document / (DF[term]))
    return IDF_Dict


#perhitungan TF-IDF
def calc_TF_IDF(LF, IDF):
    TF_IDF_Dict = {}
    for key in LF:
        TF_IDF_Dict[key] = LF[key] * IDF[key]
    return TF_IDF_Dict


with codecs.open(pathCsvFiltering, 'r',"utf-8") as f:
    for line in f:
        # print(line)
        stemWord = stemmer.stem(line)
        tokenData = nltk.word_tokenize(stemWord)
        
        # Menghitung Term Frequency 
        TF = calc_TF(tokenData)
        # csvWriterTf.writerow(TF.items())

        # Menghitung Log Frequency
        LF = calc_logFreq(TF)
        # csvWriterLf.writerow(LF.items())
        
        # Menghitung Document Frequency
        DF = calc_DF(TF)
        # csvWriterDf.writerow(DF.items())
        
        # Menghitung Inverse Document Frequency 
        n_document = 50
        IDF = calc_IDF(n_document, DF)
        # csvWriterIdf.writerow(IDF.items())
        
        # Menghitung tf-idf
        TF_IDF = calc_TF_IDF(LF, IDF)
        csvWriterTfIdf.writerow(TF_IDF.items())

        print(TF_IDF)
        print('----------------------\n')
        
        




