#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

cufflinks_output_905 = "/Users/cmdb/data/results/SRR072905_clout/genes.fpkm_tracking"
df1 = pd.read_table( cufflinks_output_905 )

cufflinks_output_906 = "/Users/cmdb/data/results/SRR072906_clout/genes.fpkm_tracking"
df2 = pd.read_table( cufflinks_output_906 )

cufflinks_output_907 = "/Users/cmdb/data/results/SRR072907_clout/genes.fpkm_tracking"
df3 = pd.read_table( cufflinks_output_907 )

cufflinks_output_908 = "/Users/cmdb/data/results/SRR072908_clout/genes.fpkm_tracking"
df4 = pd.read_table( cufflinks_output_908 )

cufflinks_output_909 = "/Users/cmdb/data/results/SRR072909_clout/genes.fpkm_tracking"
df5 = pd.read_table( cufflinks_output_909 )

cufflinks_output_911 = "/Users/cmdb/data/results/SRR072911_clout/genes.fpkm_tracking"
df6 = pd.read_table( cufflinks_output_911 )

cufflinks_output_912 = "/Users/cmdb/data/results/SRR072912_clout/genes.fpkm_tracking"
df7 = pd.read_table( cufflinks_output_912 )

cufflinks_output_913 = "/Users/cmdb/data/results/SRR072913_clout/genes.fpkm_tracking"
df8 = pd.read_table( cufflinks_output_913 )

#print df1.describe()
#print df2.describe()
#print df3.describe()
#print df4.describe()
#print df5.describe()
#print df6.describe()
#print df7.describe()
#print df8.describe()


all_files = [ cufflinks_output_905, cufflinks_output_906, cufflinks_output_907, cufflinks_output_908, cufflinks_output_909, cufflinks_output_911, cufflinks_output_912, cufflinks_output_913]
expression_levels = [] #expression levels is just an empty list to start with

for i in all_files:  
    f = open( i ) 
    while True: #this will loop forever because there is no condition. True is always true.
        line = f.readline() #this will read a line from our file, and return an empty string at the end of the file. Empty strings are always false
        fields = line.rstrip("\r\n").split("\t")
        if not line:
            break #exits the loop and goes down to the next line   
        if "Sxl" in line:
            expression_levels.append(fields[9]) #expression levels will have the column 9 contents added to it
#print expression_levels #prints the portion of the line with the expression levels in it, while it works


#before plotting, the str data in my expression levels list must be converted into integer values
int_expression = [] #integer expression levels is just an empty list to start with

for i in expression_levels:
    x = int(round(float(i)))
    int_expression.append(x)      
#print int_expression

#and now to plot the data
plt.plot(int_expression)
#fig, axes = plt.subplots(nrows=8, ncols=8)
plt.ylabel('mRNA Abundance FPKM')
#plt.setp( axes, xticks = [1, 2, 3, 4, 5, 6, 7, 8], xtickslabel=['10', '11', '12', '13', '14A', '14B', '14C', '14D'] )
plt.xlabel('Developmental Stage')
plt.show()
plt.savefig( "Homework3Graph.png" ) 
