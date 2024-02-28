import random
from Beginner.Day7_0 import stages, words, logo

target_words = words[random.randint(0,len(words))]
target_word = []
for i in target_words:
    target_word.append(i)
print(logo)
print("Welcome to the game HANGMAN!")
hidden = []
lives = len(stages)-1
for i in range(len(target_word)):
    hidden.append('_')
print(hidden)
j = True
while j == True:
    user_input = input("Enter your guess:\t").lower()
    if user_input in target_word:
        for i in range(len(target_word)):
            if target_word[i] == user_input and hidden[i]=='_':
                hidden[i] = user_input
        print("You Guessed it Right!")
        print(hidden)
    else:
        lives-=1
        s = ''
        print("You Lost a life!")
        if lives==0:
            j= False
            print("You lost the game!")
            for i in target_word:
                s+=i
            print(f"The word is\t{s}")
    print(stages[lives])
    if hidden == target_word:
        j=False
        print("You won the game!")
    else:
        continue



