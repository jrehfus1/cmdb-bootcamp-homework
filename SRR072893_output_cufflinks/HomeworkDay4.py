#!/usr/bin/env python

import pandas
import sys
import numpy
from collections import Counter
import re   

gene_ids = []
GC_ratios = []
gene_ids_indented = []
GC_ratios_indented = []
everything = {}

while 1:
    line = sys.stdin.readline()
    if line.startswith( ">"):
        gene_id = line
        gene_ids.append( gene_id )
    elif line == "":
        break
    else:
        counts = Counter(line)
        counts_GC = float(counts["C"]) + float(counts["G"])
        counts_total = float(counts["A"]) + float(counts["T"]) + float(counts["C"]) + float(counts["G"])
        GC_ratio = counts_GC/counts_total
        GC_ratios.append( GC_ratio )

#print GC_ratios   
gene_ids_indented = "\n".join( gene_ids ) 
#GC_ratios_indented = "\n".join( GC_ratios )  
#print GC_ratios_indented 
everything = zip(gene_ids, GC_ratios)
#print sorted(everything, reverse=True)
file = open("GC_Ratios.csv", "w")
for t in sorted(everything, reverse=True):
  file.write(' '.join(str(s) for s in t) + '\n')
file.close()        
        
        
    #if line.startswith( ">"):
        #parts = line.split(' ')
        #gene_name = str(parts[1])
        #chromosome_name = str(parts[2])
        #transcript_start = str(parts[3])
        #parts_transcript_start = transcript_start.split("-")
        #transcript_start_point = int(parts_transcript_start[0])
        #print transcript_start_point
        #print chromosome_name