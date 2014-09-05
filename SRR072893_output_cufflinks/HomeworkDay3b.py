#!/usr/bin/env python

#Parse one FASTA records.
#/Users/cmdb $ gtf_to_fasta /Users/cmdb/cmdb-bootcamp-homework/SRR072893_output_cufflinks/transcripts.gtf /Users/cmdb/data/genomes/dmel-all-chromosome-r5.57.fasta transcripts.fasta  #this is how I converted the transcripts file to a fasta file
import sys

line = sys.stdin.readline() #each time this appears the system will read one line. 
assert line.startswith( ">" ) #this will select lines that start with >. These are our headers 
sid = line[1:].rstrip("\r\n") #strip off the end of line characters

sequences = [] #this will accumulate my sequences
while 1: #it will loop forever. 1 = True
        line = sys.stdin.readline() #each time this appears the system will read one line. 
        if line.startswith ( ">" ): #any headers will be skipped over
            break
        else: #we will add the lines that actually have sequences to our sequences file and get rid of the white space at the ends of some of the lines
            sequences.append( line.strip() ) #the last line of the section under each header has white space at the end of it
        
sequence = "".join( sequences ) #this will concatinate each element of the list together with nothing in between because there the quotes are empty
print sid, sequence