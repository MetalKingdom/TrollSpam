#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright 2015 Overxfl0w13
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

## Preprocess utils ##
import trollutils

fileLemario        = "./Corpus/Lemario/spanishLemario.dict"
fileStopWords 	   = "./Corpus/StopWords/spanishStopWords.dict"
minChangesConst    = 1 # Min changes in levenshtein distance to break loop (if changes are lower or equal than minChangesConst, use it with caution) #
 
# Indexed alphabetically to limit search space #
def getIndexedFileAlphabetically(filePath):
	indexedFile = {}
	for a in xrange(97,123): indexedFile[chr(a)] = []
	with open(filePath,"r") as fd:
		for token in fd.readlines():
			token = token.replace('\n','')
			token = trollutils.delUpperChars(token)
			token = trollutils.removeAccents(token.decode('utf-8'))
			indexedFile[token[0]].append(token)
	fd.close()
	return indexedFile

def getIndexedStopWords(): return getIndexedFileAlphabetically(fileStopWords)
def getIndexedLemario()  : return getIndexedFileAlphabetically(fileLemario)

def delNoise(msg,lemario):
	unnoised = []
	for token in trollutils.tokenizeMe(msg):
		if token!='':
			minChanges,correctToken = float('inf'),token
			for lemToken in lemario[token[0]]:
				changes = trollutils.distanceLevenshtein(token,lemToken)
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
	msg = trollutils.delUpperChars(msg)
	# Alphanumerize message #
	msg = trollutils.alphaNumMe(msg)
	# Delete message noise #
	msg = delNoise(msg,getIndexedLemario())
	# Delete stop words #
	msg = delStopWords(msg,getIndexedStopWords())
	print msg

if __name__ == "__main__":
	preprocess("tronko no me she hable asin por diosh")
