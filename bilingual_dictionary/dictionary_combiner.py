# Combines all the dictionary files into 1 large file

import string
import sys
import codecs


alphabet = string.ascii_lowercase #'abcdefghijklmnopqrstuvwxyz'
out = "english_telugu_dictionary.csv"
out_file = codecs.open(out,"w","utf-8")
for letter in alphabet:
    with codecs.open(letter + "_telugu.csv", "r", "utf-8") as f:
        for line in f:
            combined = line.strip() + ",http://www.shabdkosh.com/te/browse\n"
            sys.stderr.write(combined)
            out_file.write(combined)
