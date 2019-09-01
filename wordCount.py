#Jebel Macias 80590537
#-Word Counter-
import sys
import re
import os
import string
import subprocess

if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input file> <output file>")
    exit()

inputFile = sys.argv[1]
outputFile = sys.argv[2]

if not os.path.exists(inputFile):
    print ("The text file input %s does not exist! Now Exiting." % inputFile)
    exit()

if not os.path.exists(outputFile):
    print ("The text file input %s does not exist! Now Exiting." % outputFile)
    exit()

def readFile():
    dict = {}
    with open(inputFile, "r") as fileReader:
        line = fileReader.read()
        line = line.split()
        for word in line:
            checkPunctuation(dict, word)

    writeFile(dict)

def checkPunctuation(dict, word):
    for char in word:
        if char in string.punctuation:
             word = word.replace(char, " ")

    line = word.split()
    for word in line:
        searchDictionary(dict, word)

def searchDictionary(dict, word):
    if word == "":
        return
    word = word.lower()
    if word in dict:
        dict[word] += 1
    else:
       dict[word] = 1

def writeFile(dict):
    fileW = open(outputFile, "w")
    for word, number in sorted(dict.items()):
        fileW.write(word + " " + str(number)+ "\n")

readFile()
