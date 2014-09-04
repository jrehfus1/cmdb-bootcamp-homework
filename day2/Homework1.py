#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

cufflinks_output_m = "/Users/cmdb/cmdb-bootcamp-homework/day2/SRR072893_clout/genes.fpkm_tracking"

df = pd.read_table( cufflinks_output_m )

cufflinks_output_f = "/Users/cmdb/cmdb-bootcamp-homework/day2/SRR072915_clout/genes.fpkm_tracking"

df2 = pd.read_table( cufflinks_output_f )


#Step one is to count the number of rows in each file:
#males:
fm = open( cufflinks_output_m )

nlm = 0
while True: #this will loop forever because there is no condition. True is always true.
    line = fm.readline() #this will read a line from our file, and return an empty string at the end of the file. Empty strings are always false
    if line == "":
        break #exits the loop and goes down to the next line   
    else:
        nlm = nlm +1
print nlm
a = nlm/3
b = 2*a

#females:
ff = open( cufflinks_output_f )

nlf = 0
while True: #this will loop forever because there is no condition. True is always true.
    line = ff.readline() #this will read a line from our file, and return an empty string at the end of the file. Empty strings are always false
    if line == "":
        break #exits the loop and goes down to the next line   
    else:
        nlf = nlf +1
print nlf
x = nlm/3
y = 2*a

#now we will sort everything in the FPKM columns in descending order, and save it into new files
males = df.sort( "FPKM", ascending = False )
females = df2.sort( "FPKM", ascending = False )

males.to_csv( "cufflinks_output_m.csv", sep="\t", index=False ) 
females.to_csv( "cufflinks_output_f.csv", sep="\t", index=False ) 

#now we will make three files, dividing the sorted data into the top third, middle third, and bottom third based on the total number of rows in the data set. 
males1 = males[0:a]
males2 = males[a:b]
males3 = males[b:nlm]

females1 = females[0:x]
females2 = females[x:y]
females3 = females[y:nlf]

#print males1.describe()
#print males2.describe()
#print males3.describe()
#print females1.describe()
#print females2.describe()
#print females3.describe()  

#plt.ylabel("Density")
#plt.xlabel("FPKMs")

#now it's time to actually make the plots
data = males1, males2, males3, females1, females2, females3
#labels = ["M1, M2, M3, F1, F2, F3"]
plt.boxplot(data)
