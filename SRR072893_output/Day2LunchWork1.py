#!/usr/bin/env python

samfilefromcufflinks = "//Users/cmdb/cmdb-bootcamp-homework/SRR072893_output/accepted_hits.sam"

f = open( samfilefromcufflinks )

nl = 0
for line in f: #this will count the number of lines in our file that start with SRR
    if "SRR" in line:
        nl = nl + 1 
print nl