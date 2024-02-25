line1 = ['[D]','[D]','[D]']
line2 = ['[D]','[D]','[D]']
line3 = ['[D]','[D]','[D]']
map = [line1,line2,line3]
position = input("Give a position to hide the Treasure\t")
row,column = position[1],position[0]
#print(row,column)
if column == 'A':
    column= 0
elif column == 'B':
    column= 1
else:
    column = 2
#print(column)
map[int(row)][column] = 'X'
print("Now the treasure is hidden!")
x = input("Do you want to see the treasure?\t")
if x.casefold() == 'yes' or x.casefold()=='y':
    print(f'{line1}\n{line2}\n{line3}')