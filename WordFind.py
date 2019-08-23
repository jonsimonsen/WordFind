#imports
import subprocess

#Get user input
targetWord = ''
#targetWord = input("Enter a search word (or just enter to quit): ")

#Initializing variables
targetFile = 'testfile.txt'
#targetLine = '^' + targetWord + '$'
targetLine = ''
searching = True

#Try to find the word
while searching == True:
    targetWord = input("Enter a search word (or just enter to quit): ")
    if targetWord == '':
        searching = False
    else:
        targetLine = '^' + targetWord + '$'
        subprocess.call(['grep', '-n', targetLine, targetFile])

print("Good Bye!")
