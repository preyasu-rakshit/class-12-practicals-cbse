#Write a python program that read only first 10 characters of a file “test.txt”.

with open('test.txt', 'r') as f:
    out = f.read(10)

print(out)