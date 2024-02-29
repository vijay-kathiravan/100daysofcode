import random
from Beginner.Day11_0 import logo
print("Welcome to Black Jack Game!")
print(logo)
continue_game = True
def draw(x,flag=1):
    for i in range(flag):
        x.append(random.randint(1,10))
def check_stand():
    if (sum(dealer_list) > sum(player_list)) and sum(dealer_list) <= 21:
        starting_move(1)
        print("You lost!")
    elif sum(dealer_list) < 17:
        draw(dealer_list)
        check_stand()
    elif sum(dealer_list) > 21:
        starting_move(1)
        print("You Win")
    elif sum(dealer_list) == sum(player_list):
        print("Push")
    else:
        starting_move(1)
        print("You Win")
def check_hit():
    draw(player_list)
    starting_move(1)
    if sum(player_list) > 21:
        print("You Lost the game")
    else:
        user_inp()

def starting_move(flag):
    if flag ==2:
        draw(player_list,flag)
        draw(dealer_list,flag)
        flag-=1
        print(f"Dealers card is {dealer_list[0]}")
        print(f"Your cards are {player_list}")
        print(f"Total: {sum(player_list)}")
    else:
        print(f"Dealers cards are {dealer_list}")
        print(f"Your cards are {player_list}")
        print(f"Total: {sum(player_list)}")
def user_inp():
    user_choise = input("Do you want to stand or hit?\t").casefold()
    if user_choise == 'stand':
        check_stand()
    elif user_choise == 'hit':
        check_hit()

while continue_game:
    player_list = []
    dealer_list = []
    flag = 2
    inp = input("Do you want to play Black Jack Game? Types Yes or No\t").casefold()
    if inp == 'yes':
        starting_move(flag)
        user_inp()
    else:
        continue_game = False






