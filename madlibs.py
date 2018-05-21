#! /usr/bin/python
# madlibs.py - Takes a text file and replaces the words ADJECTIVE, NOUN, 
# ADVERB, and VERB with user input. Like Mad Libs.

import sys, os.path

# Open text file if it exists
if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]) == False:
        print("File does not exist")
        sys.exit(0)
else:
    print("Please provide the name of an input text file \n \'madlibs.py <filename>\'")

txtFile = open(sys.argv[1])

madLibFile = open("MadLibbed-" + sys.argv[1], 'w')

# Scan the file for occurrences of ADJECTIVE, NOUN, ADVERB, or VERB
# When a keyword is found, prompt the user for a replacement word
txtFileContent = txtFile.read()

txtFileWords = txtFileContent.split()
index = 0

for word in txtFileWords:
    if "ADJECTIVE" in word:
        madlib = input("Enter and adjective: ")
        txtFileWords[index] = word.replace("ADJECTIVE", madlib)
    elif "NOUN" in word:
        madlib = input("Enter a noun: ")
        txtFileWords[index] = word.replace("NOUN", madlib)
    elif "ADVERB" in word:
        madlib = input("Enter an adverb: ")
        txtFileWords[index]= word.replace("ADVERB", madlib)
    elif "VERB" in word:
        madlib = input("Enter a verb: ")
        txtFileWords[index]= word.replace("VERB", madlib)
    index += 1

# Put the input into a new file

madLibContents = ' '.join(txtFileWords)
madLibFile.write(madLibContents)

txtFile.close()
madLibFile.close()
