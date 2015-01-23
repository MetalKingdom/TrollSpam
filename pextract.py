#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright 2015 Overxfl0w13
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

import trollutils
fileNoSpam = "./Corpus/NoSpam/nospamlist.dict"
fileSpam   = "./Corpus/Spam/spamlist.dict"
fileTroll  = "./Corpus/Troll/trollist.dict"

# Save hash tables with frequency of all tokens and a list for 50 most frequent terms #
hashNoSpam       = {}
hashSpam         = {}
hashTroll        = {}
listMostNoSpam   = []
listMostSpam     = []
listMostTroll    = []
# (k+4)-dimensional vectors (4 for user information and 50 for frequency of 50 tokens of text) #
hashPerceptron   = {}
dimensions       = 30 # + 4 (A low value recommended in early learning stages) #

def generateHashTable(hashTable,filePath):
	with open(filePath) as fd:
		hashTokens,countTokens     = [],0
		fd.readline() # Avoid format explanation #
		for hashLine in fd.readlines():
			hashTokens.append(trollutils.removeStringFromList(trollutils.tokenizeMe((trollutils.alphaNumMe(hashLine[hashLine.rfind('| '):]))),''))
		hashTokens = trollutils.flattenerList(hashTokens)
		countTokens = len(hashTokens)
		# Add token to hashSpam token with its frequency #
		for token in hashTokens: hashTable[token] = float(hashTokens.count(token))/countTokens
	fd.close()
	
def getKMoreFrequent(hashTable,k):
	# It's horrible to give order to a hash table is, use priority queue (priority -> frequency token) #
	return trollutils.sortHashTable(hashTable)[0:k]

if __name__ == "__main__":
	generateHashTable(hashTroll,fileTroll)
	generateHashTable(hashSpam,fileSpam)
	generateHashTable(hashNoSpam,fileNoSpam)
	listMostNoSpam = getKMoreFrequent(hashNoSpam,dimensions)
	listMostSpam   = getKMoreFrequent(hashSpam,dimensions)
	listMostTroll  = getKMoreFrequent(hashTroll,dimensions)
	#print str(len(listMostNoSpam))+","+str(len(listMostSpam))+","+str(len(listMostTroll))
	#print listMostNoSpam
	#print listMostSpam
	#print listMostTroll
