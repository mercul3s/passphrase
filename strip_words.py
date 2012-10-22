#!/usr/bin/python
from sys import argv
import string
import os
'''
	This script should be used for stripping words out of a list of words and definitions. 
	An input and output file must be specified on the command line as this script takes two args.
	Currently, definitions must be separated by a colon and in the following form:

	A
	Word: definition
	Word: definition 
	B
	Word: definition
	...etc

	First, read open the file for reading, and split into a list on newlines.
	Then loop through the list, and pull out the words and definitions separately 
	(Definitions may used at a later date.) Finally, add just the words to a file, 
	each one on a separate line.
'''
readfile = argv[1]
writefile = argv[2]
def main(read, write):

	# open text we want to store
	f = open(read)
	words = f.read()
	f.close()
	# split on newlines - returns a list of words and definitions
	words = words.splitlines()
	stripchars = ('')
	
	# will be used to store words and definitions
	word_dict = {}
	# if item in list is not an empty string or single letter, 
	# split it and copy the word and definition as a key value pair to word_dict
	for word in words:
		if len(word) > 1:
			word = word.split(':')
			# work around for blank lines and single characters
			try:
				word_dict[(word[0])] = word[1]
			except:
				print "only one item in list, skipping."
				continue
	
	# write our words to a new file without definitions
	g = open(write, 'a')
	for key, value in word_dict.iteritems():

		print "Word: ", key
		print "Definition: ", value
		if stripchars in key:
			wordalt = key.split(',')
			g.write(wordalt[0].replace(' ', '' ) + '\n')
		else:
			g.write(key + '\n')
	g.close()

main(readfile, writefile)


