#!/bin/bash

#
# Day 1 - Homework: Part 2 - debug this bash script
# This should output commands for all 24???

echo "There are around 6 mistakes"

FASTQ_DIR=/Users/cmdb/data/fastq
OUTPUT_DIR=/Users/cmdb/data/day1

GENOME_DIR=/Users/cmdb/data/genomes
SRP0729=SAMPLE_PREFIX
=dmel5 #shouldn't something go in front of this?
ANNOTATION=dmel-all-r5.57.gff

CORES=4

for i in 24{01..16}$FASTQ_DIR $OUTPUT_DIR $GENOME_DIR $CORES $ANNOTATION #added the variables that had been defined here
do #added this
  echo fastqc $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR
  echo tophat 
  echo cufflinks
done #added this