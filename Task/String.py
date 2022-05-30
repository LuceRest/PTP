import nltk
import string
import re

bulan = "Bulan Febuari"
print(bulan[3])
print()

bulan1 = "Bulan Januari"

print([s.lower() for s in bulan1])
print([s.upper() for s in bulan1])
print([s.replace('a', 'O') for s in bulan1])
print()


kata = 'aku suka kamu'
kata2 = 'sekalii'

print(kata[5])
print(kata.replace('m', 'o'))
print(kata.upper())
print(kata.join(kata2))
print(kata.lower())
print()

kata3 = 'akusukakamusekalii'
print(re.findall(r'[aiueo]', kata))
print()

print(re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'usually'))
print()

print(re.findall(r'^(.*)(di|ke|per)$', 'dimasa'))
print(re.findall(r'(ber|ke|per)(.*)$', 'presentasikan'))
print(re.findall(r'((ber|ke|per|di)(.*))$|(.*)(an)$', 'dimasakan'))
print()

for i in re.split(' ', kata):
    print(i)
print()

kalimat1 = 'Aku )))benci kamu$#$ tetapi cinta juga&&&&'
hasil = kalimat1.translate(str.maketrans("", "", string.punctuation))
print(hasil)
print()


