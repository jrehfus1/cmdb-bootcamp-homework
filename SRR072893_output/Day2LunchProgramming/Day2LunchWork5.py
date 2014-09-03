#!/usr/bin/env python

samfilefromcufflinks = "//Users/cmdb/cmdb-bootcamp-homework/SRR072893_output/accepted_hits.sam"

f = open( samfilefromcufflinks )

for i, line in enumerate( f ):
    fields = line.rstrip("\r\n").split("\t") 
    
x = sorted( fields[2] )

list = x #change this to a list of strings
    
from collections import Counter
input =  list
c = Counter( input )

print( c.items() )