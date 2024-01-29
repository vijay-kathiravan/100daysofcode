print("Hello, Welcome to the tip calculator\n")
Total_bill = int(input("What is the total bill?\t$"))
Tip_percentage = int(input("What percentage tip would you like to give 5, 10, 15 or 20?\t"))
Total_after_tip =Total_bill + ( Total_bill * (Tip_percentage/100))
split_by = int(input("Is the bill being split? If yes then how many people are splitting the bill?\t"))
Each_pay = round(Total_after_tip/split_by,2)
print("Each person have to pay ${}".format(Each_pay))

