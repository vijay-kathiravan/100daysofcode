print("We are going to calculate the highest score from a list of scores")
maxx = 0
list_of_scores = input("Enter the list of scores!\t").split(',')
for i in range(0, len(list_of_scores)):
    list_of_scores[i] = int(list_of_scores[i])
    if list_of_scores[i] > maxx:
        maxx = list_of_scores[i]
print(f"The maximum score is {maxx}")
