__author__ = 'mekides123'
with open('C:/Users/mekides123/Desktop/file/health.txt') as infile:
    dictionary = {line.strip().lower() for line in infile}

print("----Linear search-----")
with open('C:/Users/mekides123/Desktop/file/health.txt') as infile:
    for i,line in enumerate(infile, 1):
        line = line.strip()
        words = split_line(line) # your split_line function
        for word in words:
            if word.lower() not in dictionary:
                print("Line ", i, ": probably misspelled: ", word)

from bs4 import BeautifulSoup
import urllib.request
import nltk
response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
tokens = [t for t in text.split()]
freq = nltk.FreqDist(tokens)
for key,val in freq.items():
    print (str(key) + ':' + str(val))