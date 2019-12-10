# -*- coding: utf-8 -*-
"""
Created on Wed Sep 04 09:46:58 2019

@author: admin
"""
import spellchecker
#from spellchecker import spellchecker
dir(spellchecker)
format(spellchecker)
"<class 'spellchecker.spellchecker.spellchecker'>"

spell= spellchecker()
#sugestion = spellchecker()
files = ["come","bads","recive","geverment"]
for word in file:
    print ('{spell.correction(word)}')
    print ('{{spell.candidates(word)}')
    #print (f'{word}:{spell.suggestion(word)}')