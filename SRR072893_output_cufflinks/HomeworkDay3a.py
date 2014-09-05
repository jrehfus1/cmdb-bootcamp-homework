#!/usr/bin/env python

import re
import sys
import numpy as np
#must write <transcripts.gtf in order to get it to read the right file
ex_start = []
ex_end = []
int_ex_start = []
int_ex_end = []
everything = {}
totalexonlength = []
totalexonlist = []
int_total_exons = []
attributes = []
while 1:
    line = sys.stdin.readline() #each time this appears the system will read one line. 
    if "exon_number " in line:
        parts = line.split('\t')
        exon_start = str(parts[3])
        exon_end = str(parts[4])
        ex_start.append( exon_start )
        ex_end.append( exon_end )
    elif "C" in line:
        for i in ex_start:
            x = int(i)
            int_ex_start.append(x)
        startarray = np.array(int_ex_start)
        for i in ex_end:
            y = int(i)
            int_ex_end.append(y)  
        endarray = np.array(int_ex_end)
        exonlength = endarray - startarray
        totalexonlength = sum(exonlength)
        totalexonlist.append(totalexonlength)
        del ex_start[:]
        del ex_end[:]
        del int_ex_start[:]
        del int_ex_end[:]
        parts = line.split('\t')
        attribute = str(parts[8])
        attributes.append( attribute )
    elif line == "":
        break
             
attributes_indented = "\n".join( attributes )
everything = zip(totalexonlist, attributes)
file = open("newfile.txt", "w")
for t in sorted(everything, reverse=True):
  file.write(' '.join(str(s) for s in t) + '\n')
file.close()