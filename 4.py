#Write a python program to read the file “test.txt” line by line.

with open('test.txt', 'r') as f:
    while True:
        line = f.readline()
        
        if not line:
            break
        
        print(line, end="")