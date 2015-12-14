# Import the subprocess module.
import subprocess
from subprocess import Popen, PIPE, STDOUT
import os.path, sys
import struct
import re

#the file that the user is ging to input
dnaFolder = sys.argv[1]
dnaName = sys.argv[2]
outputFolder = sys.argv[3]

    #####################################################
    #                    MAIN                           #
    #####################################################

def main():
    #determine DNA type from pdb file
    DNAtype=obtainDNAtype()
    #obtain the sequence
    DNAseq=obtainDNAseq()
    #run x3DNA
    runx3DNA(DNAtype, DNAseq)
    print "DNAtype" + DNAtype

    #####################################################
    #                    DNAtype                        #
    #####################################################

    
def obtainDNAtype():
#open the new file
    pdb_file = open(dnaFolder+dnaName+".pdb")
    pdb_lines = pdb_file.readlines()
    pdb_file.close()

    #create a variable to hold the DNA fiber type
    DNAtype=""
    alreadyFoundType = False

    for line in pdb_lines:
        if line.startswith("TITLE" or "KEYWDS"):
            varZ = find_sub_string("Z-DNA", line)
            varB = find_sub_string("B-DNA", line)
            varA = find_sub_string("A-DNA", line)

            if varZ==True:
                DNAtype = "B-DNA"
                alreadyFoundType = True
            if varB==True:
                DNAtype = "B-DNA"
                alreadyFoundType = True
            if varA==True:
                DNAtype = "A-DNA"
                alreadyFoundType = True

    if(alreadyFoundType==False):
        DNAtype= "B-DNA"

    return DNAtype

#
#function obtained from: http://stackoverflow.com/questions/7361253/python-how-to-find-a-substring-in-another-string
#I have also made some changes
#
def find_sub_string(word, string):
    len_word = len(word)
    for i in range(len(string)-1):
        if string[i: i + len_word] == word:
            return True

    return False

    #####################################################
    #                    DNAseq                         #
    #####################################################

    
def obtainDNAseq():    
    #open the new file
    fasta_file = open(dnaFolder+dnaName+".fasta")
    fasta_lines = fasta_file.readlines()
    fasta_file.close()

    #create a variable to hold the DNA sequence
    DNAseq=""

    for line in fasta_lines:
        #identify the sequence from the fasta file
        if not line.startswith(">"):
            newline=str(line)
            DNAseq= newline.replace("\n","")
    return DNAseq

    #####################################################
    #                    x3DNA                          #
    #####################################################
    

def runx3DNA(DNAtype, DNAseq):
    if (DNAtype=="B-DNA"):
        pref = "-b"
    elif (DNAtype=="A-DNA"):
        pref = "-a"
    elif (DNAtype=="Z-DNA"):
        pref = "-z"

    #command obtained from fiber -help
    createFiber = ["fiber","-seq=" + DNAseq, pref, outputFolder+dnaName+".x3DNA.pdb"]
    subprocess.call(createFiber)

main()
