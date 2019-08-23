# WordFind
-Program for finding words in scrabble dictionaries (or more generally matching lines in text files).  
-Will only find lines that exactly match the input, so make sure the text files and input are formatted accordingly.  
-Do not inject actual code into the input, since I can not guarantee that poor input will not damage the system the program is run on. Standard English letters [a-z] and [A-Z] should be fine, but use the program at your own risk.  

# Installing and running
-The program contains subprocess calls, and i do not guarantee that your system is safe while running this program.  
-The program uses Python 3, so install this.  
-Fork the repo. I suggest keeping the forked files together in a folder that does not contain other files.  
-Run the program from terminal by typing: python3 ./Wordfind.py  

# Version history
test version: Only searches for a specific word in a specific file

# Version 0.1
-Accepts input of words from the user  
-Restricts hits by applying anchors to the input  
-Keeps running until the user enters no input (just enter)  

# TODOs
4: Let the user specify the name of the input file  
5: Optionally try to prevent access to folders outside of where the program resides (to prevent damage from potential ignorant or malicious user input)  
