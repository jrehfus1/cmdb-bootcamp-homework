#!/usr/bin/env python

samfilefromcufflinks = "//Users/cmdb/cmdb-bootcamp-homework/SRR072893_output/accepted_hits.sam"

f = open( samfilefromcufflinks )

for i, line in enumerate( f ):
    fields = line.rstrip("\r\n").split("\t") 
    if i > 16: #this leaves out the first line, which is just headers for the subsequent lines
        print fields[2] #this acts a lot like cut, choosing the fifth column of each line in our file