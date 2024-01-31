Height = float(input("Hi there! To calculate your BMI, "
                     "Kindly provide your height in centimeter's\t"))
weight = float(input("Kindly provide your weight in Kg's!\t"))
BMI = int(weight/((Height/100)**2))
print("Your BMI is " + str(BMI))
if BMI < 18.5:
    print("You are under weight!")
elif 18.5 <= BMI < 25:
    print("You have a normal weight!")
elif 25 <= BMI < 30:
    print("You are slightly over weight!")
elif 30<= BMI < 35:
    print("You are obese!")
else:
    print("You are clinically obese!")
