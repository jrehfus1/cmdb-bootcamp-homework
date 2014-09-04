#!/usr/bin/env python
import re
import sys

sequence_names = [] #this will accumulate my sequences
id_ratio = []
gp_ratio = []
ratios = []
#ids_and_gaps = {}
everything = {}
fly_genes = []
while 1: #it will loop forever. 1 = True
        line = sys.stdin.readline() #each time this appears the system will read one line. 
        if line.startswith ( ">" ): #any empty lines will be skipped over
            sequence_names.append( line.strip() ) 
        elif "Identities" in line:
            parts = line.split(' ')
            identity_ratio = str(parts[3])
            gap_ratio = str(parts[7])
            id_ratio.append( identity_ratio )
            gp_ratio.append( gap_ratio )
        elif line.startswith ("Query="):
            parts = line.split(' ')
            fly_gene = str(parts[3])
            fly_genes.append( fly_gene )
        elif line == "": #the last line of the file starts with white space
            break
            
sequence = "\n".join( sequence_names ) #this will concatinate each element of the list together with nothing in between because there the quotes are empty
#identity = "\n".join( identity_names )
#identities = "\n".join ( id_ratio )
#gaps = "\n".join ( gp_ratio )
#ids_and_gaps = zip(identities, gaps)
everything = zip(sequence_names, id_ratio, gp_ratio) #this puts my three lists together to make a tuple
#print everything
#print sequence
#print identity
#print identities
#print gaps
print fly_genes
#print "\n".join(str(sequence) + ': ' + str(identity) for sequence, identity in merged_list) #this will print my tuple where each pair gets its own line so that its easier to read
#print "\n".join(str(sequence) + ': ' + 'identity ratio is: ' + str(id_ratio) + ' and the gaps ratio is: '+ str(gp_ratio) for sequence, id_ratio, gp_ratio  in everything)
#print "\n".join(str(sequence) + '\t' + str(id_ratio) + '\t' + str(gp_ratio) for sequence, id_ratio, gp_ratio  in everything)