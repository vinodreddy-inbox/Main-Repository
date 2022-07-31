# To install textblob module on windows -> py -m pip install textblob
from textblob import TextBlob
def Convert(string):
    li = list(string.split())
    return li

str1 = input("Enter your sentence : ")
words = Convert(str1)
corrected_words = []

for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words :", words)
print("Corrected Words are :")
for i in corrected_words:
    print(i.correct(), end=" ")

