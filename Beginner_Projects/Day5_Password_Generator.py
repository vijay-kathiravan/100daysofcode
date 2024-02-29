import random

print("Welcome to Password Generator!")
letters = int(input("How many letters would you like your password to have?\t"))
numberss = int(input('How many numbers would you like your password to have? \t'))
symbols = int(input("How many symbols would you like your password to have?\t"))
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbolss = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
pswd=[]
print(letter[random.randint(0,len(letter)-1)])
for i in range(letters):
    pswd.append(letter[random.randint(0,len(letter)-1)])
for j in range(numberss):
    pswd.append(number[random.randint(0,len(number)-1)])
for k in range(symbols):
    pswd.append(symbolss[random.randint(0,len(symbolss)-1)])
random.shuffle(pswd)
print(pswd)
ps = ''
for i in range(len(pswd)):
    ps += pswd[i]
print(ps)
