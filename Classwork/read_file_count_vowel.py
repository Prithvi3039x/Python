filename = "C:/2_PYTHON/Classwork/sample.txt"

vowels = "aeiouAEIOU"
count = 0

f = open(filename, 'r')
text = f.read()

for char in text:
    if char in vowels:
        count += 1

print(count)