import random

print("Welcome to the Rock, Paper, Scissor Game! Let's Play!")
choise = int(input("What do you want to choose Rock, Paper or Scissor?\n Rock - 1, Paper - 2, Scissor -3\t"))
rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
if choise == 1:
    print(rock)
    print("You chose Rock")
elif choise == 2:
    print(paper)
    print("You chose Paper")
else:
    print(scissor)
    print("You chose Scissor")
computer_choise = random.randint(1,3)
if computer_choise == 1:
    print(rock)
    print('Computer chose Rock')
elif computer_choise == 2:
    print(paper)
    print('Computer chose Paper')
else:
    print(scissor)
    print('Computer chose Scissor')
if (choise == 1 and computer_choise == 1) or (choise==2 and computer_choise==2) or (choise==3 and computer_choise==3) :
    print("It's a draw")
elif(choise==1 and computer_choise==3) or (choise==2 and computer_choise==1) or (choise==3 and computer_choise==2):
    print('You Win! Winner, Winner, Chicken dinner!')
elif(computer_choise==1 and choise==3) or (computer_choise==2 and choise==1) or (computer_choise==3 and choise==2):
    print('Computer Wins!')
print('Thanks for playing')