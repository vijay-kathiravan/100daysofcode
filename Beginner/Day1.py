# Vijay
var = input('Give a word to count the number of strings in it!\n')
red1 = 0
for i in var:
    if i in var:
        red1+=1
print(red1)