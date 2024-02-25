import random

names = input("Who are all in the party?\t")
names_to_be_fed = names.split(',')
bill = random.randint(0,len(names_to_be_fed)-1)
print("{} will be paying today's bill".format(names_to_be_fed[bill]))
