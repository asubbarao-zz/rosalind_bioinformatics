#http://rosalind.info/problems/dna/
from collections import Counter 
import pandas as pd


def count_dna_sequence(path_to_textfile):

  data = pd.read_csv(path_to_textfile)  #pandas thinks each character is a column and passes an empty dataframe
  dna_string = data.columns[0] #access the string 
  counted_bases = Counter(dna_string)

  return counted_bases

path_to_textfile = input("Enter filepath to the DNA sequence .txt file ")
print zip(count_dna_sequence(path_to_textfile).keys(), count_dna_sequence(path_to_textfile).values())