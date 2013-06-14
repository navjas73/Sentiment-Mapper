import re, math, collections, itertools, os
import nltk, nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
import subprocess

class Sentiment():
	
	def _init_(self):
		#from affin readme:
		afinn = dict(map(lambda (k,v): (k,int(v)), [ line.split('\t') for line in open("AFINN-111.txt") ]))
	

	def evaluate_text_afinn(self):
		# sample from affin readme:
		# returns -5 (very negative) to +5 (very positive)
				
		x = sum(map(lambda word: afinn.get(word, 0), text.lower().split()))
		infile = open('sentiment.csv', 'rb')
		print x


	def evaluate_text_sanan(self):
	    subprocess.Popen("workingsentiment.py", shell=True)


