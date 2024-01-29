Height = float(input("Hi there! To calculate your BMI, "
               "Kindly provide your height in centimeter's\t"))
weight = float(input("Kindly provide your weight in Kg's!\t"))
BMI = str(int(weight/((Height/100)**2)))
print("Your BMI is " + BMI)
