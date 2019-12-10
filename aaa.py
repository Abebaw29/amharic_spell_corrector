import string
import difflib
import logging
import spellchecker
from spellchecker import SpellChecker
import nltk
from nltk.metrics import edit_distance
import re
import glob
import codecs
import math
import time
import spellchecker
starting_time=time.clock()
from operator import itemgetter
class Amharic_Inverted_file:
   def inverted(self,path):
      def readDocContents(filename):
         indexterms=[]
         each_doc_terms=codecs.open(filename, encoding='utf-8')
         doc_terms=each_doc_terms.readlines()
         each_doc_terms.close()
         for terms in doc_terms:
            if terms.endswith('\n'):
              terms=terms.rstrip('\n')
              indexterms.append(terms)
         return indexterms
def punctuationMarkRmv(terms):
         terms=re.sub('[" ፣ : / ? () ። ፤ - ]','',terms)
         if terms.endswith('\n'):
              terms=terms.rstrip('\n')
         if terms.startswith(' '):
              terms=terms.lstrip(' ')
         s=codecs.open("am.txt",'r', encoding = 'utf-8' )
         puc = s.read()
         for pc in puc:
              if terms.endswith(pc):
                terms=terms.rstrip(pc)
              if terms.startswith(pc):
                terms=terms.lstrip(pc)
         return terms
def docPath(path):
         allDocPath=[]
         infile=open(path)
         doc_path=infile.readlines()
         infile.close()
         for doc_list in doc_path:
            if doc_list.endswith('\n'):
               doc_list=doc_list.rstrip('\n')
            allDocPath.append(doc_list)
         return allDocPath

class SpellingReplacer(object):
    def __init__(self, dict_name = 'en_GB', max_dist = 2):
        self.spell_dict = enchant.Dict(dict_name)
        self.max_dist = 2

    def replace(self, word):
        if self.spell_dict.check(word):
            return word
        suggestions = self.spell_dict.suggest(word)

        if suggestions and edit_distance(word, suggestions[0]) <= self.max_dist:
            return suggestions[0]
        else:
            return word
    
#word = ("ነው","አቶ","ውስጥ","ቀን","ወደ","ጋር",'መሆኑን")

def word_check (s):
    for word in s.casefold().split():
        if word not in words:
            suggestion = difflib.get_close_matches(word, words)
#print(f' did you mean {",".join (str(x)for x in suggestion)} instead of {word}')
s= input('input string:')
word_check(s)
