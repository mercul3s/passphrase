#!/usr/bin/python

'''
This script will take a list of words, file specified on the command line,
ask user for the number of words desired in the passphrase, and will return
the random word passphrase with punctuation inserted between the words.
Future improvements may include incorporating this into a web page, and asking
what kind of slang to use as the base for the passphrase, checking to see the 
security of the generated passphrase, and also giving the definitions for the 
words used in the passphrase.
'''

import random
from sys import argv
import string

# open file passed as arg, split on newlines, and return list of words
readfile = argv[1]
def open_file(filename):
	f = open(filename)
	words = f.read()
	f.close()
	words = words.split('\n')
	return words

# pass in list of words, prompt user for length, and return passphrase
def gen_pw(word_list):
	punctuation = string.punctuation
	pass_len = int(raw_input('Enter passphrase length: '))
	passphrase = ""
	for length in xrange(pass_len):
		passphrase += random.choice(word_list) + random.choice(punctuation)
	return passphrase

# call the two functions above and output passphrase to screen
def main():
	w_list = open_file(readfile)
	passphrase = gen_pw(w_list)
	print passphrase

main()