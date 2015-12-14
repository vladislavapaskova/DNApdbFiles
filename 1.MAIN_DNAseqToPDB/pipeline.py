
#Vladislava Paskova
#Creating DNA fibers using x3DNA software

'''This file will create pdb files for a given DNA sequence
'''

# Import the subprocess module.
import subprocess
import os.path, sys

    #####################################################
    #                      MAIN                         #
    #####################################################

def main():

    #get DNA type --> part 1
    DNAtype = obtainDNAtype()

    DNAseq = ""
    #only obtain sequence if it is not one of the special DNA fiber types (they have their own specific sequence)
    if(isSpecialStructures(DNAtype)==False):
        #get DNA sequence --> part 2
        DNAseq = obtainDNAseq()

    #get output file path --> part 3
    outputFilePath = getOutputFile()

    #create DNA fiber using x3DNA --> part 4
    createFiber(DNAtype, DNAseq, outputFilePath)

    #visualize in Jmol
    # Build the JMol command
    jmolCommand = ["java", "-jar", "./Jmol.jar",outputFilePath+".pdb", "-ij", "background white"]
    subprocess.call(jmolCommand)


    #####################################################
    #                    MESSAGES                       #
    #####################################################

DNATYPEMESSAGE="\n******************\nDNA fiber type: \n 1 -> enter through the terminal \n 2 -> path to pdb file to extract it from \n help -> view all of the 55 different types of fibers.\n q -> quit.\n******************\n"
DNATYPECHOICE="\n******************\nInput the type of DNA fiber(A-DNA/B-DNA/Z-DNA)\nor\nenter DNA fiber number(1-55)\n******************\n"
DNATYPECHOICE1="\n******************\nPlease enter a path to the PDB file that contains the type of the DNA fiber (e.g. /Users/Documents/1CBU.pdb):\n******************\n"
DNASEQUENCE="\n******************\nDNA sequence:\n1->input the DNA sequence through the terminal\n2->give a path to an existing file\nq->quit\n******************\n"
DNASEQUENCE1="\n******************\nPlease input the sequence. Note you can only use A, T, G, C capitalized. No nonstandard nucleotides can be used in this program\n******************\n"

            
    #####################################################
    #     Part 1: Define the type of DNA fiber          #
    #####################################################
    
def obtainDNAtype():
    DNAtype = ""
    
    #choice of how to obtain the DNA type
    defOrPDB =  raw_input(DNATYPEMESSAGE)
    while not (defOrPDB=='1' or defOrPDB=='2' or defOrPDB=='q'or defOrPDB=='help'):
        print("\n******************\nThe requested command ("+defOrPDB+") is not valid.\n")
        defOrPDB=raw_input("\nPlease enter '1','2', 'help' or 'q'\n******************\n")

    if (defOrPDB == 'q'):
        quit()
        
    #print list of fibers and then asks user to input DNA type
    if (defOrPDB == 'help'):
        printListFiber()
        DNAtype = getTypeThroughInput()
        
    #asks user to input DNA type
    if (defOrPDB == '1'):
        DNAtype = getTypeThroughInput()
        
    #get type from pdb file
    if (defOrPDB == '2'):
        # Ask the user for a path to the pdb file that contains the type of the fiber
        filePath = raw_input(DNATYPECHOICE1)

        # Make sure that the file exists
        filePath = checkIfFileExists(filePath)

        print("\n******************\nExtracting DNA type form inputted PDB file \n******************\n")
        DNAtype = extractFromPDB(filePath)
    
    print("\n******************\nThe DNA fiber type is "+ DNAtype + ".\n******************\n")
    return DNAtype 


#asks user to input a correct DNA type
def getTypeThroughInput():
    DNAtype = raw_input(DNATYPECHOICE)
    while (checkIfDNAtypeIsCorrect(DNAtype)==False):
        print("\n******************\nThe type you entered (" + DNAtype + ") does not exist.\n")
        DNAtype = raw_input("\nPlease input a correct fiber type (or type 'q' to quit):\n******************\n")
        if (DNAtype == 'q'):
            quit()
    return DNAtype

#prints the list of different fiber types
def printListFiber():
    print("\n******************\nPlease refer to this list\n******************\n")
    fibertypeHelp = ["fiber", "-m", "help"]
    subprocess.call(fibertypeHelp)
    print("\n\n")   
    
#extract DNA type from pdb file
def extractFromPDB(filePath):
    fileTypeFiberReader = open(filePath, 'r+')
    DNAtype = ""
    alreadyFoundType = False
    for line in fileTypeFiberReader:
        if line.startswith("TITLE" or "KEYWDS"):
            varZ = find_sub_string("Z-DNA", line)
            varB = find_sub_string("B-DNA", line)
            varA = find_sub_string("A-DNA", line)

            if varZ==True:
                DNAtype = "Z-DNA"
                alreadyFoundType = True
            if varB==True:
                DNAtype = "B-DNA"
                alreadyFoundType = True
            if varA==True:
                DNAtype = "A-DNA"
                alreadyFoundType = True
    if alreadyFoundType==False:
        print("\n******************\nThe DNA fiber type could not be identified from the PDB file please input a valid DNA fiber type\n******************\n")
        DNAtype = getTypeThroughInput()
    fileTypeFiberReader.close()  
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
    #     Part 2: Get input sequence                    #
    #####################################################


def obtainDNAseq():
    print("\n\n")
    seq = raw_input(DNASEQUENCE)
    while not (seq=='1' or seq=='2' or seq=='q'):
        print("\n******************\nThe requested command ("+seq+") is not valid.\n")
        seq=raw_input("\nPlease enter '1','2' or 'q'\n******************\n")
    
    if (seq == 'q'):
        quit()

    if (seq == '1'):
        DNAseq = getSeqThroughInput()

    if (seq == '2'):
        fileType = raw_input("\n******************\nDNA sequence file type:\n1->input a text file\n2->input a FASTA file\nq->quit\n******************\n")
        while not (fileType=='1' or fileType=='2' or fileType=='q'):
            print("\n******************\nThe requested command ("+fileType+") is not valid.\n")
            fileType=raw_input("\nPlease enter '1','2' or 'q'\n******************\n")

        if (fileType == 'q'):
            quit()

        if (fileType == '1'):
            fileTypeSeq = raw_input("\n******************\nPlease give a path to the text file(e.g. /Users/Documents/example.txt):\n******************\n")
            # Make sure that the file exists
            fileTypeSeq = checkIfFileExists(fileTypeSeq)
            #get sequence from text file
            DNAseq = getSeqFromTextFile(fileTypeSeq)

        #if it is a FASTA file
        if (fileType == '2'):
            fileTypeSeq = raw_input("\n******************\nPlease give a path to the FASTA file(e.g. /Users/Documents/example.fasta.txt):\n******************\n")
            # Make sure that the file exists
            fileTypeSeq = checkIfFileExists(fileTypeSeq)
            DNAseq = getSeqFromFastaFile(fileTypeSeq)
    
    return DNAseq

#ask user to input DNA sequence
def getSeqThroughInput():
    DNAseq = raw_input(DNASEQUENCE1)
    while(checkIfSeqCorrect(DNAseq)==False):
        print("\n******************\nThe sequence you entered (" + DNAseq + ") does not exist.\n")
        DNAseq = raw_input("\nPlease input a correct sequence.\n******************\n")
    return DNAseq

#get sequence from text file
def getSeqFromTextFile(filePath):
    #reding from the text file to get the sequence
    fileSeqReader = open(filePath , 'r+')
    for line in fileSeqReader:
        if not line=="":
            newline=str(line)
            DNAseq= newline.replace("\n","")
        else:
            print("\n******************\nThe DNA sequence could not be identified from the text file please input a valid DNA sequence\n")
            DNAseq = getSeqThroughInput()
    fileSeqReader.close()
    return DNAseq

# read from FASTA file to get the sequence
def getSeqFromFastaFile(filePath):
    fileSeqReader = open(filePath , 'r+')
    for line in fileSeqReader:
        #identify the sequence from the fasta file
        if not line.startswith(">"):
            newline=str(line)
            DNAseq= newline.replace("\n","")
            while(checkIfSeqCorrect(DNAseq)==False):
                print("\n******************\nThe sequence you entered (" + DNAseq + ") does not exist.\n")
                DNAseq = raw_input("\nPlease input a correct sequence.\n******************\n")
    fileSeqReader.close()
    return DNAseq


    #####################################################
    #     Part 3: Name DNA fiber ; give path to dir     #
    #####################################################


#get output file to store the new DNA structure
def getOutputFile():
    print("\n\n")
    path = raw_input("\n******************\nPlease give a name for the output file (e.g. 1YUI)or type 'q' to quit:\n******************\n")
    if (path == 'q'):
        quit()
    return path

    #####################################################
    #     Part 4: Create DNA fiber                      #
    #####################################################


#creates the DNA fiber; needs DNAtype, DNAseq, outputFilePath
def createFiber(DNAtype, DNAseq, outputFilePath):
    print("\n\n")
    print("\n******************\nThe DNA fiber will be created and output in the given folder\n******************\n")

    if (DNAtype=="B-DNA"):
        pref = "-b"
    elif (DNAtype=="A-DNA"):
        pref = "-a"
    elif (DNAtype=="Z-DNA"):
        pref = "-z"
    else:
        pref = "-"+DNAtype

    #command obtained from fiber -help
    #where repeats.txt contains the number of repeats only
    #if (pref=="-a")or (pref=="-b")or (pref=="-1")or (pref=="-4")or (pref=="-7")or (pref=="-46")or (pref=="-47")or (pref=="-53")or (pref=="-54")or(pref=="-55"):
    if(not isSpecialStructures(DNAtype)):
        createFiber = ["fiber","-seq=" + DNAseq, pref, outputFilePath+".pdb"]
        subprocess.call(createFiber)
    else:
        number_repeats = raw_input ("\n******************\nPlease enter the number of repeats.\n******************\n")
        output_file = open("./numberOfRepeats.txt", "w")
        output_file.write(str(number_repeats))
        output_file.close()
        createFiber = ["fiber", pref, outputFilePath+".pdb"]
        subprocess.call(createFiber, stdin=open("./numberOfRepeats.txt"))


    #####################################################
    #                Helper Functions                   #
    #####################################################
#function that checks if one of the special DNA fiber structures is chosen
def isSpecialStructures(pref):
    if (pref=="A-DNA")or (pref=="B-DNA")or (pref=="1")or (pref=="4")or (pref=="7")or (pref=="46")or (pref=="47")or (pref=="53")or (pref=="54")or(pref=="55"):
        return False
    return True

#function checks if the sequence is only comprised of A,T,G,C
def checkIfSeqCorrect(DNAseq):
    listSeq = list(DNAseq)
    result = True
    for l in listSeq:
        if not (l=="A" or l=="T" or l=="G" or l=="C"):
            result = False
    return (result)

#function checks if the inputted DNA type is correctly spelled
def checkIfDNAtypeIsCorrect(DNAtype):
    if(DNAtype=="A-DNA" or DNAtype=="B-DNA" or DNAtype=="Z-DNA"):
        return True
    else:
        for i in range(1,55):
            if DNAtype== str(i):
                return True
    return False

#quits
def quit():
    print("Exiting.")
    sys.exit(0) # exit the system if the user types q

#checks if file exists
def checkIfFileExists(filePath):
    while not os.path.isfile(filePath):
        print("\n******************\nThe file you entered (" + filePath + ") does not exist.\n")
        filePath = raw_input("\nPlease enter a path to an existing file (or type 'q' to quit): \n******************\n")
        if (filePath == 'q'):
            quit()
    return filePath



main()

