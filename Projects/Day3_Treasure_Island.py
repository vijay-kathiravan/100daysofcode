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
Direction = input("Do you want to go left or right?\t")
if Direction.lower() == 'left':
    action = input("Do you want to swim or wait?\t")
    if action.lower() == 'wait':
        door = input("Which door do you want to open? Red, Blue, Yellow?\t")
        if door.lower() == 'yellow':
            print('You Win!')
        else:
            print("Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over")
