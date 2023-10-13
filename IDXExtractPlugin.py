from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os
import argparse

class IDXExtractPlugin:
 def input(self, inputfile):
     self.INPUT_FASTA = inputfile
 def run(self):
     pass
 def output(self, outputfile):
     OUT_DIR = outputfile

     if not os.path.exists(OUT_DIR):
       os.mkdir(OUT_DIR)

     for record in SeqIO.parse(self.INPUT_FASTA, "fasta"):
       sequence_attributes = record.description.split("_")
       print(sequence_attributes)
       GENOME_NAME = sequence_attributes[1] + "_" + sequence_attributes[2] + "_" + sequence_attributes[4]

       OUT_FASTA=OUT_DIR + "/" + GENOME_NAME + ".fna"

       with open(OUT_FASTA, "w") as f:
         SeqIO.write(record, f, "fasta")
