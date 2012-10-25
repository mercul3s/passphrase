import random
import string

def open_file(filename):
	f = open(filename)
	words = f.read()
	f.close()
	words = words.split('\n')
	return words

# pass in list of words, prompt user for length, and return passphrase
def gen_pw(length, word_list):
	punctuation = string.punctuation
	passphrase = ""
	for length in xrange(length):
		passphrase += random.choice(word_list) + random.choice(punctuation)
	return passphrase
