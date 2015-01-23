#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright 2015 Overxfl0w13
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

## Preprocess utils ##
import unicodedata
import string
tchr,tord          = chr,ord
fileLemario        = "spanishLemario.dict"
fileStopWords 	   = "spanishStopWords.dict"
minChangesConst    = 1 # Min changes in levenshtein distance to break loop (if changes are lower or equal than minChangesConst, use it with caution) #

def delUpperChars(msg): return "".join([tchr(tord(x)+32) if tord(x) in xrange(65,91) else x for x in msg ])
def alphaNumMe(msg): return "".join([x if (x.isalpha() or x==' ') else '' for x in msg])
def tokenizeMe(msg): return msg.split(' ')
def remove_accents(data): return ''.join(x for x in unicodedata.normalize('NFKD', data) if x in string.ascii_letters).lower()

# Source: http://es.wikipedia.org/wiki/Distancia_de_Levenshtein#Python #
def distanceLevenshtein(str1, str2):
	d=dict()
	for i in range(len(str1)+1):
		d[i]=dict()
		d[i][0]=i
	for i in range(len(str2)+1):
		d[0][i] = i
	for i in range(1, len(str1)+1):
		for j in range(1, len(str2)+1):
			d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+(not str1[i-1] == str2[j-1]))
	return d[len(str1)][len(str2)]
 
# Indexed alphabetically to limit search space #
def getIndexedLemario():
	lemario = {}
	for a in xrange(97,123): lemario[chr(a)] = []
	with open(fileLemario,"r") as fd:
		for token in fd.readlines():
			token = token.replace('\n','')
			token = delUpperChars(token)
			token = remove_accents(token.decode('utf-8'))
			lemario[token[0]].append(token)
	fd.close()
	return lemario
	
# Indexed alphabetically to limit search space #
def getIndexedStopWords():
	stopWords = {}
	for a in xrange(97,123): stopWords[chr(a)] = []
	with open(fileStopWords,"r") as fd:
		for token in fd.readlines():
			token = token.replace('\n','')
			token = delUpperChars(token)
			token = remove_accents(token.decode('utf-8'))
			stopWords[token[0]].append(token)
	fd.close()
	return stopWords
	
def delNoise(msg,lemario):
	unnoised = []
	for token in tokenizeMe(msg):
		if token!='':
			minChanges,correctToken = float('inf'),token
			for lemToken in lemario[token[0]]:
				changes = distanceLevenshtein(token,lemToken)
				if(changes<minChanges):
					minChanges,correctToken = changes,lemToken
				if(changes<minChangesConst): break
			unnoised.append(correctToken)
	return unnoised
		
def delStopWords(msg,stopWords):
	unStopWords,find = [],False
	for token in msg:
		for stopWord in stopWords[token[0]]:
			if token==stopWord: find = True	
		if find==False: unStopWords.append(token)
		find = False
	return unStopWords
	
def preprocess(msg):
	# Delete upper case chars #
	msg = delUpperChars(msg)
	# Alphanumerize message #
	msg = alphaNumMe(msg)
	# Delete message noise #
	msg = delNoise(msg,getIndexedLemario())
	# Delete stop words #
	msg = delStopWords(msg,getIndexedStopWords())
	print msg

if __name__ == "__main__":
	preprocess("tronko no me des eshe rejalo que me descongojo enthero shuprimo")
