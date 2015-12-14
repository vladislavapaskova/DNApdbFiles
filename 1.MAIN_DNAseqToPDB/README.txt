Vladislava Paskova

Build the 3D DNA structure from plain DNA sequences (whose 3D structure may not be already known in PDB)

Invokes the external program x3DNA

It is an interactive pipeline with many options along the way.

1. DNA fiber type: 
-enter it through the terminal
-give a path to a pdb file to extract it from
-option to invoke x3DNA’s library and show all of the different types of DNA fibers included

2.DNA sequence:
-input the DNA sequence through the terminal
-give a path to an existing file (it can be either a txt file or a fasta file) 

3.Give a path to the output file

Note: If we are dealing with one of the special DNA fiber types, then the sequence if predefined by the program thus the user is not asked to input it. But the user needs to input the number of repeats. 

It creates a new pdb file reconstructing the 3D DNA structure using the external program (executable) x3DNA.

