def get_max(*num):
    if len(num) == 0:
        return None
    max_num = num[0]
    for i in num:
        if i > max_num:
            max_num = i
    return max_num

def get_longest(*args):
    if len(args) == 0:
        return None
    longest = args[0] 
    for i in args:
        if len(i) > len(longest):
            longest = i
    return longest


print(get_max(1,2,3,52,1,123,52,11))
print(get_longest("atharv","prithvi","Abhilasha"))