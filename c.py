# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 08:43:48 2019

@author: admin
"""
!pip install packages SymSpell
import nltk
import sys
import codecs
import difflib
def readfile(filename):
    txtfile = open("am.txt","r",encoding='utf-8')
    txtfile = infile.readlines()
print(txtfile.name)
txtfile.close
    
   
import difflib
def word_check(s):
    if word not in txtfile:
        suggestion = difflib.get_close_matches(word, txtfile)
        print(f" did you mean {"," for x in suggestion} instad of {words}")
        s= input('input string')        
        word_check(s)
        