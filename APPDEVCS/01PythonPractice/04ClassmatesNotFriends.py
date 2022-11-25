classmates = ["C1", "C2", "C3", "F1", "F2"]
friends = ["F1", "F2", "F3"]

classmates_not_friends = set(classmates) - set(friends)

result = list(classmates_not_friends)
print(result)

# or

classmates_not_friends = list(filter(lambda x: x not in friends, classmates))
print(classmates_not_friends)