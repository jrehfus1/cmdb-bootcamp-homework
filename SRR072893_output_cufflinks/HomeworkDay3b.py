#!/usr/bin/env python

#Parse one FASTA records.
#/Users/cmdb $ gtf_to_fasta /Users/cmdb/cmdb-bootcamp-homework/SRR072893_output_cufflinks/transcripts.gtf /Users/cmdb/data/genomes/dmel-all-chromosome-r5.57.fasta transcripts.fasta  #this is how I converted the transcripts file to a fasta file
import sys

start_codon1 = "ATG"
start_codon2 = "GTA"
stop_codon1 = "TGA"
stop_codon2 = "TAG"
stop_codon3 = "TAA"
stop_codon4 = "AGT"
stop_codon5 = "GAT"
stop_codon6 = "AAT"

#if start codon one and one of the first three stop codons are in the same frame, print
#if start codon two and one of the last three stop codons are in the same frame, print

#line = sys.argv[1]#sys.stdin.readline() #each time this appears the system will read one line. 
#assert line.startswith( ">" ) #this will select lines that start with >. These are our headers 
#sid = line[1:].rstrip("\r\n") #strip off the end of line characters

#ORF = [] #this will accumulate my sequences
while 1: #it will loop forever. 1 = True
        line = sys.argv[1]#sys.stdin.readline() #each time this appears the system will read one line. 
        if line.startswith ( ">" ): #any headers will be skipped over
            pass
        elif start_codon1 in line: #and stop_codon1 line start_codon1[1]:
            for i in range(0, len(line), 3):
                if i == start_codon1 or start_codon2:
                    print i
                else:
                    break
        else:
            break            
        
            #ORF.append( line.strip() ) #the last line of the section under each header has white space at the end of it
        #elif line == "":
            #break
            
#ORFS = "".join( ORF ) #this will concatinate each element of the list together with nothing in between because there the quotes are empty
#print sid, ORF
#print start_codon[1]