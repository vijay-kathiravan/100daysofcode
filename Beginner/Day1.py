# Vijay
var = input('Give a word to count the number of strings in it!\n')
flag = 0
for i in var:
    if i in var:
        flag+=1
print(flag)