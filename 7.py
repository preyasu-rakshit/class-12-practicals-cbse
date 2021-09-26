# Write a python program to display the total number of lines in the
# given file “TEST.txt”.

with open('test.txt', 'r') as f:
    lines = f.readlines()
    count = len(lines)

print(count)