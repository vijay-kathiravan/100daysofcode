print("Printing the sum of even numbers in a range of numbers")
ra = int(input("Give the max of the range to which we have to calculate the sum\t"))
sa = 0
for i  in range(0,ra+1):
    if i%2==0:
        sa += i
print(f"The sum is {sa}")