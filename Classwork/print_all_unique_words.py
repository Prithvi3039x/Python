filename = "C:/2_PYTHON/Classwork/sample.txt"

f = open(filename, 'r')
text = f.read()
f.close()

words = text.split()
unique_words = list(set(words))

print(f"Unique words: {unique_words}")
print(f"Total unique: {len(unique_words)}")