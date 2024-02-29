print("""
,d
88
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  ,adPPYba,
88      88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8 a8P_____88
88      88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88        8PP"""""""
88,     88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88         "8b,   ,aa
"Y888   88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          `"Ybbd8"'


                                                 88
 88                         88                   88
 88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88
 88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88
 88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88
 88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88
 88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8""")

print("Welcome to Treasure Island! Your Mission is to find the treasure!")
Direction = input("You are at a crossroad! Do you want to go left or right?\t")
if Direction.lower() == 'left':
    action = input("You have come to a Lake, there is an island in the middle of the lake! "
                   "Type wait to wait for a boat or swim to swim across the lake?\t")
    if action.lower() == 'wait':
        door = input("You arrived at the island unharmed!"
                     "There is a house with three doors! Which door do you want to open? Red, Blue, Yellow?\t")
        if door.lower() == 'yellow':
            print('You found the treasure!  4You Win!')
        else:
            print("It's a room full of fire! Game Over!")
    else:
        print("An Angry trout attacked you! Game Over!")
else:
    print("You fell into a hole! Game Over!")
