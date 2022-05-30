import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB

def read_file(filename):
    data = pd.read_csv(filename)
    print(data.shape)
    data['label'] = data['label'].apply(lambda x: x.strip().lower())
    return data



datatrain = 'D:/Kuliah Online/Pemrosesan Teks Praktik/9th Meet/1st Session (Monday, April, 18th 2022)/Practice/Data/mandalika21032022_edit1_cleanbobot401.csv'
datatest = 'D:/Kuliah Online/Pemrosesan Teks Praktik/9th Meet/1st Session (Monday, April, 18th 2022)/Practice/Data/mandalika29032022_hapususer30_cleanLABELING.csv'


data_ho_train = read_file(datatrain)
data_ho_test = read_file(datatest)


target_encoder = LabelEncoder()
data_ho_train['targetTR'] = target_encoder.fit_transform(data_ho_train['label'])
data_ho_test['targetTS'] = target_encoder.transform(data_ho_test['label'])
data_ho_train.head()


x_ho_train = data_ho_train.drop(['tweet_clean','label'], axis=1)
y_ho_train = data_ho_train['targetTR']
#x_ho_train.head()
x_ho_test = data_ho_test.drop(['tweet_clean','label'], axis=1)
y_ho_test = data_ho_test['targetTS']
#x_ho_train.head()


vectorizer = TfidfVectorizer (max_features=2500)
model_g = GaussianNB()

v_data = vectorizer.fit_transform(data_ho_train['tweet_clean']).toarray()
print (v_data)


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(v_data, data_ho_train['label'], test_size=0.1, random_state=0)      # test_size yg semula 0.2 dirubah menjadi 0.1
model_g.fit(X_train,y_train)


y_preds = model_g.predict(X_test)

print(confusion_matrix(y_test,y_preds))
print(classification_report(y_test,y_preds))
print('nilai akurasinya adalah ',accuracy_score(y_test, y_preds))