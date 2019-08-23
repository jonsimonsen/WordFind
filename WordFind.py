#imports
import subprocess

#Initializing variables
targetFile = 'testfile.txt'
targetWord = 'test'
targetline = 'test\n'

#Try to find the word
subprocess.call(['grep', targetFile, targetWord])
