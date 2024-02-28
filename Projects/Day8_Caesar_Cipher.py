print("Welcome to Caesar Cipher Tool")
def encode_decode(choise:str,string:str,shift:int)->str:
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                 'w', 'x', 'y', 'z',
                 '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                 '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '~', '-', '_', '=', '+',
                 '[', '{', ']', '}', '\\', '|', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?']
    newlist = ''
    if choise == 'encode':
        for i in string:
            index = -(len(alphabets))
            index += alphabets.index(i)
            newlist+= alphabets[shift+index]
    else:
        for i in string:
            index = -(len(alphabets))
            index += alphabets.index(i)
            newlist+= alphabets[-shift+index]
    return  newlist

flag = True
while flag ==True:
    enc = encode_decode(input("Enter whether you want to encode or decode\t"),input("\nEnter the word you want to encode or decode\t"),
                          int(input("\nEnter the shift!\t")))
    print(enc)
    cont = input("Do you want to keep encoding or decoding?\t")
    if cont == 'Yes'.casefold():
        pass
    else:
        break
