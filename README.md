passphrase
==========

A passphrase generator and utility for stripping words out of a list of words and definitions.

strip_words.py:

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

passphrase.py:

This script will take a list of words, file specified on the command line,
ask user for the number of words desired in the passphrase, and will return
the random word passphrase with punctuation inserted between the words.
Future improvements may include incorporating this into a web page, and asking
what kind of slang to use as the base for the passphrase, checking to see the 
security of the generated passphrase, and also giving the definitions for the 
words used in the passphrase.