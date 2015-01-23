#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright 2015 Overxfl0w13
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
import unicodedata,string,operator
tchr,tord,tlist          = chr,ord,list

def removeStringFromList(lst,string): return [x for x in lst if x!=string]
def delUpperChars(msg) 				: return "".join([tchr(tord(x)+32) if tord(x) in xrange(65,91) else x for x in msg ])
def alphaNumMe(msg)					: return "".join([x if (x.isalpha() or x==' ') else '' for x in msg])
def tokenizeMe(msg)    				: return msg.split(' ')
def removeAccents(msg)				: return ''.join(x for x in unicodedata.normalize('NFKD', msg) if x in string.ascii_letters).lower()
def flattenerList(lst) 				: return [item for sublist in lst for item in sublist]
def prettyPrint(string)				: return "Building if it's necessary..."
def sortHashTable(x)   				: return tlist(reversed(sorted(x.items(), key=operator.itemgetter(1))))

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
