#!/usr/bin/env python

#Parse multiple different FASTA records.
import sys
from fasta import FASTAReader #now I don't need all of my code in this file, I just pull it from another file that is not itself executable
        
reader = FASTAReader( sys.stdin )  
#while 1: #unnecessary with our stopiteration line
    #sid, sequence = reader.next() #take the returned value and assign it to a new sid and sequence
for sid, sequence in reader:
    print sid, sequence