#! /usr/bin/python
# regexDirSearch.py - Searches all the .txt files in a directory for any line 
# that matches a user-supplied regular expression. Returns the results to the 
# standard output.

import re, os

# Compile user supplied regular expression
if len(sys.argv) != 2:
    print('''
    Please supply a regular expression
    \'regexDirSearch.py "<regex>"\'
    '''

# TODO: Determine a list of files to search

# TODO: Checks each line for a match to the supplied regex

# TODO: Print out the matched line.
