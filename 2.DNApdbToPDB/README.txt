Vladislava Paskova

Reconstruct 3d DNA structure for already known data from PDB
Used for testing the external code x3DNA


This program takes 2 files (retrieved from from the PDB databank):
- a .pdb file containing a DNA fiber —> to obtain DNA type (A-DNA, B-DNA or Z-DNA)
- its corresponding .fasta file —> to obtain DNA sequence

(Note:If the fiber type cannot be extracted from the pdb file then B-DNA is used as a default.Also if DNA type is Z-DNA since x3DNA assumes a GC repeat only the program  reassigns a B-DNA fiber type)


It creates a new pdb file (in the output directory) reconstructing the 3d DNA structure using the external program (executable) x3DNA.

Run:

python solve.py ./input/1D8G/ 1D8G ./output/

1. Takes path to a directory that contains all of the needed files,{.pdb, .fasta}, name of DNA fiber, and path to output directory 
2. Runs x3DNA
3. Outputs 1D8G.x3DNA.pdb in Output
