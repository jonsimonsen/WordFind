#imports
import subprocess

#Initializing variables
targetFile = 'testfile.txt'
targetWord = 'test'
targetLine = '^test$'

#Try to find the word
subprocess.call(['grep', '-n', targetLine, targetFile])
