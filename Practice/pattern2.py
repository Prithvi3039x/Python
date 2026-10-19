for i in range(1,6):  # for each row
    for j in range(1,6 - i): # for each row print spaces that are: total rows -1
        print(" ", end="") # after each space the end will be "" so no default new line

    for j in range(2 * i -1): # to print stars for each row according to row number
        print("*",end="")
    print() # after one row go to new line
        