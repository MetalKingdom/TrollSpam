#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright 2015 Overxfl0w13
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

# Perceptron #

def vectorxvector(v,y):
	s = 0
	for n in xrange(len(v)):
		s += v[n] * y[n]
	return s
	
def vectorxconstant(v,a):
	return [x*a for x in v]

def vectordifference(v,y):
	return [v[n]-y[n] for n in xrange(len(v))]

def vectorsum(v,y):
	return [v[n]+y[n] for n in xrange(len(v))]	

			  # Vectores de peso iniciales #
weightVectors = [] # Vectores de peso iniciales #
nameVectors   = []
			  # Muestras de entrenamiento #

learnSamples          = []
recognizementSamples  = []

alpha         = 0.00001; # Factor de aprendizaje #
b             = 0.00001; # Margen #
maxLimit      = 10000;

def perceptron():
	m             = 0;
	c             = 0;
	while(m<len(learnSamples) and c<maxLimit):
		m = 0 
		c += 1
		for n in xrange(len(learnSamples)):
			i = learnSamples[n][1]
			g = vectorxvector(weightVectors[i],learnSamples[n][0])
			error = False
			for j in xrange(len(weightVectors)):
				if(j!=i):
					if(vectorxvector(weightVectors[j],learnSamples[n][0]) + b > g):
						weightVectors[j] = vectordifference(weightVectors[j],vectorxconstant(learnSamples[n][0],alpha))
						error = True
			if error: weightVectors[i] = vectorsum(weightVectors[i],vectorxconstant(learnSamples[n][0],alpha))
			else: m += 1	
	if(c==maxLimit): return False

def generar_colores(numclasses):
	return [plot_colours.pop(randint(0,len(plot_colours)-1)) for x in xrange(numclasses)]
	
def perceptron_recognizement():
	recognizeds = []
	for sample in recognizementSamples:
		maxim,i = -float('inf'),0
		for iv in xrange(len(weightVectors)):
			prod = vectorxvector(weightVectors[iv],sample)
			if prod > maxim:
				maxim = prod
				i = iv
		recognizeds.append((sample,i))
	return recognizeds

if __name__ == '__main__':
	perceptron()
	recognizeds = perceptron_recognizement()		
