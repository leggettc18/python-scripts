#! /usr/bin/python
# regexDirSearch.py - Searches all the .txt files in a directory for any line 
# that matches a user-supplied regular expression. Returns the results to the 
# standard output.

import re, os, sys

# Compile user supplied regular expression
if len(sys.argv) != 2:
    print("""Please supply a regular expression
    \'regexDirSearch.py "<regex>"\'""")
    sys.exit(0)

regex = re.compile(r'' + sys.argv[1])

# Determine a list of files to search
cwd = os.getcwd()
fileList = os.listdir(cwd)
txtFileList = []
for file in fileList:
    if file.endswith(".txt"):
        txtFileList.append(file)

# Checks each line for a match to the supplied regex

for file in txtFileList:
    # Open the file
    txtFile = open(file, 'r')
    # Check each line for matches
    lines = txtFile.readlines()
    for line in lines:
        if regex.search(line) != None:
            # Print out the matched line.
            print(line)
    # Close the file
    txtFile.close()
