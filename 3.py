# Write a Python program that read a file “test.txt” and display all the
# contents of the file using readline() function. (SUPPOSE FILE HAS
# FOUR LINES).

with open('test.txt', 'r') as f:
    for i in range(4):
        line = f.readline()
        print(line, end="")
