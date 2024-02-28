def prime_number_checker(number:int)->bool:
    """
    This function checks if the given number is a prime number or not
    :param number: This parameter takes a integer number as an input
    :return: This function returns a boolean value saying whether the number given is a prime number or not
    """
    flag = 0
    for i in range(2,number+1):
        if number%1==0 and number%i==0:
            flag+=1
    if flag>1:
        return False
    else:
        return True


prime = prime_number_checker(int(input("Enter a number to check if it is prime\t")))
print(prime)
