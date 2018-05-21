#! /usr/bin/python
# mcb.pyw - saves and loads pieces of text to the clipboard
# Usage: mcb.pyw save <keyword> - Saves clipboard to keyword.
#        mcb.pyw <keyword> - Loads keyword to clipboard
#        mcb.pyw list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb.shelf')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# Delete clipboard content
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del(mcbShelf[sys.argv[2]])
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    # Delete all keywords
    elif sys.argv[1].lower() == 'delete':
        for keyword in mcbShelf:
            del mcbShelf[keyword]

mcbShelf.close()
