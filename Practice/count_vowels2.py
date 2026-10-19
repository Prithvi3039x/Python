vowels = ['a','e','i','o','u']
s = input("Enter a string: ")
count_a,count_e,count_i,count_o,count_u = 0,0,0,0,0

for i in s:
    for j in vowels:
        if i == j:
            if i == 'a':
                count_a += 1
            elif i == 'e':
                count_e += 1
            elif i == 'i':
                count_i += 1
            elif i == 'o':
                count_o += 1
            elif i == 'u':
                count_u += 1
print("Count of a: ",count_a)
print("Count of e: ",count_e)
print("Count of i: ",count_i)
print("Count of o: ",count_o)
print("Count of u: ",count_u)