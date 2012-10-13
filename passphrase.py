'''
open dictionary file, choose 4 random words from file, insert punctuation
'''
import random
import sys
import string

def open_file():
	f = open('/usr/share/dict/words')
	words = f.read()
	f.close()
	words = words.split()
	return words

def gen_pw(word_list):
	punctuation = string.punctuation

	f = open('/usr/share/dict/words')
	word_list = f.read()
	word_list = word_list.split()

	pass_len = 3

	passphrase = ""
	for length in xrange(pass_len):
		passphrase += random.choice(word_list) + random.choice(punctuation)
	print passphrase
def main():
	w_list = open_file()
	gen_pw(w_list)
main()