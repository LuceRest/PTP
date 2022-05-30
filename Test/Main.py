import nltk
# import matplotlib.pyplot as plt

# nltk.download()

text = '''Welcome to the hell. Lets start with our first tutorial on NLTK. We shall leaern the basics of NLTK here.add()'''

from nltk.tokenize import word_tokenize

word_tokenized = word_tokenize(text)
print(f'word_tokenized : {word_tokenized} \n----------------------\n')




