name1 = input("Welcome to Love Calculator!\n Kindly provide the name of Romeo!\t")
name2 = input("Kindly provide name of Juliet!\t")
true1= love1 = 0
name1+=name2
for i in name1:
    if i.upper() in 'TRUE':
        true1+=1
    if i.upper() in 'LOVE':
        love1+=1
score = int(str(true1)+str(love1))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print("Your score is {}, you are alright together.".format(score))
else:
    print("Your score is {}.".format(score))
