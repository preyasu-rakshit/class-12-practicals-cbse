#Write a python program that count the occurrence of “Is” in the file “STUDY.TXT”.

count = 0
with open("study.txt", 'r') as f:
    content = f.read()
    words = content.split()
    for word in words:
        if word.lower() == 'is':
            count += 1

print(count)