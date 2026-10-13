sentence = input("Enter a sentence: ")

words = sentence.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print(f"Words list: {words}")
print(f"Longest word: {longest}")