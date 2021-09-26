#Write a python program to count the number of occurrences of
# ‘the’ and ‘this’ in the given file “STUDY.txt”.


count = 0
with open('study.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            if word.lower() == 'the' or word.lower() == 'this':
                count += 1

print(count)