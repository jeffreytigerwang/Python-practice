# Python code to
# demonstrate readlines()

L = []

# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()

# Using readlines()

file1 = open('myfile.txt', 'r')

Lines = file1.readlines()



count = 0
# Strips the newline character

print(Lines)