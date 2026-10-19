for i in range(1,6):  # for each row
    for j in range(1,6 - i): # for each row print spaces that are: total rows -1
        print(" ", end="") # after each space the end will be "" so no default new line
    if i % 2 == 0: #if row number is even print row with "*"
        symbol = "*"
    else:          #if row number is not even print row with "#"
        symbol = "#"
    for j in range(2 * i -1): # to print stars for each row according to row number
        print(symbol,end="")
    print() # after one row go to new line