#!/usr/bin/env python

samfilefromcufflinks = "//Users/cmdb/cmdb-bootcamp-homework/SRR072893_output/accepted_hits.sam"

f = open( samfilefromcufflinks )

nl = 0
for line in f: #this will loop forever because there is no condition. True is always true.
    if "HI:i:0" in line: #HO i is the number of perfect hits
        nl = nl + 1 
print nl