#Write a python program that count the number of lines in the file
# ‘COMPUTER.TXT’ that start with ‘A’.

count = 0
with open('computer.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if line[0] in "Aa":
            count += 1

print(count)