#!/usr/bin/env python

samfilefromcufflinks = "//Users/cmdb/cmdb-bootcamp-homework/SRR072893_output/accepted_hits.sam"

f = open( samfilefromcufflinks )

nl = 0
for line in f: #this will loop forever because there is no condition. True is always true.
    if "NH:i:1" in line: #NH i where i is the number of reported alignments that contains the query in the current record
        nl = nl + 1 
print nl