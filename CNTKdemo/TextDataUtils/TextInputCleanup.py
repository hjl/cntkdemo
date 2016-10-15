#   TextInputCleanup.py
#
#   start with an input text file
#   generate a mapping file of input symbols to integers
#   generate an output file of integer sequences
#
#   some things to do in ASCII character map
#       keep alphanumeric and punctuation (decimal 32 to 127)
#       replace CR (13), NL (10) sequences with NL only (10)
#       replace FF (12) with NL (10) only
#       replace Tab (8) with 4 * Space (32)
#       append Period (46) with <End Of Sentence> when followed by any whitespace or new line
#       replace 3 * Period (46) with <Ellipsis>
#
#   

import os, string, nltk, getopt
from datetime import datetime


class TextInputCleanup:

    def __init__(self):
        self.rawtext = None
        self.filename = None
        self.filehandle = None
        return
        

    def Read(self, filename):
        self.filename = filename
        self.filehandle = open(filename)
        self.rawtext = filehandle.read()
        return


if __name__ == '__main__':
    print("running standalone test")

    inputfilename = r"c:\\local\\testdata\\book-corpus\\blah.txt"
    tic = TextInputCleanup()
    tic.Read(inputfilename)
