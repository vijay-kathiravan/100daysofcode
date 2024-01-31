year = int(input("Provide a year to check if that year is a leap year or not!\t"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a Leap Year!")
        else:
            print(f"{year} is a not a Leap Year!")
    else:
        print(f"{year} is a Leap Year!")
else:
    print(f"{year} is not a Leap Year!")