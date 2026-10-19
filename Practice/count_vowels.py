vowels = ['a','e','i','o','u']
s = input("Enter a string: ")
count = 0
for i in s:
    for j in vowels:
        if i == j:
            count+=1
print(count)

