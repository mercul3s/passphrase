#!/usr/bin/python

'''
open dictionary file, choose 4 random words from file, insert punctuation
'''
import random
from sys import argv
import string

readfile = argv[1]
def open_file(filename):
	f = open(filename)
	words = f.read()
	f.close()
	words = words.split('\n')
	return words

def gen_pw(word_list):
	punctuation = string.punctuation
	pass_len = int(raw_input('Enter passphrase length: '))
	passphrase = ""
	for length in xrange(pass_len):
		passphrase += random.choice(word_list) + random.choice(punctuation)
	print passphrase
	return passphrase

def main():
	w_list = open_file(readfile)
	gen_pw(w_list)
main()