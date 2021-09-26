# Write a python FUNCTION to count the number of vowels in the given file “TEST.TXT”.


def count_vowels():
    count = 0
    with open('test.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            for letter in line:
                if letter in 'aeiouAEIOU':
                    count += 1

    return count

print(count_vowels())
