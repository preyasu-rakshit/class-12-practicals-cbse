# Write a python program to find the total no of digits in the file “TEST.TXT”.

count = 0
with open('test.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        for letter in line:
            if letter.isdigit():
                count += 1

print(count)