# WordFind
-The program contains subprocess calls, and i do not guarantee that your system is safe while running this program.
-Program for finding words in scrabble dictionaries (or more generally matching lines in text files).
-Will only find lines that exactly match the input, so make sure the text files and input are formatted accordingly.
-Do not inject actual code into the input, since I can not guarantee that poor input will not damage the system the program is run on. Standard English letters [a-z] and [A-Z] should be fine, but use the program at your own risk.

# Version history
test version: Only searches for a specific word in a specific file

# TODOs
1: Accept input of words from user
2: Restrict hits by applying anchors to the input
3: Keep running until the user enters no input (just enter)
4: Let the user specify the name of the input file.
5: Optionally try to prevent access to folders outside of where the program resides (to prevent damage from potential ignorant or malicious user input).
