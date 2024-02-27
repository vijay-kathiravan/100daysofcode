print("Welcome to Python pizza Shop!")
size = input("Kindly enter what size pizza you want to order! Small(S),Medium (M) or Large(L)?")
add_pepperoni = input("Kindly enter if you would like to add pepperoni on top of your pizza! Yes(Y) or No(N)?")
add_extra_cheese = input("Kindly enter if you would like to add extra cheese to your pizza! Yes(Y) or No(N)?")
Bill = 0
if size =='S':
    Bill+= 15
elif size == 'M':
    Bill+= 20
else:
    Bill+= 25
if add_pepperoni=='Y' and size=='S':
    Bill+=2
elif add_pepperoni=='Y' and size!='S':
    Bill+=3
else:
    pass
if add_extra_cheese=='Y':
    Bill+=1
print(f"You have to Pay ${Bill} for your pizza")

