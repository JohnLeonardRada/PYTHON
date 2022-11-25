lucky_numbers = [4, 8, 10, 15, 18, 21]
friends = ["Johnny", "Leonard", "Leonard", "Yanfei", "Zhongli", "Peter"]

#Using append function/adds a new data to the list
friends.append("Apollo")
print(friends)

#Using extend function/connects the two list
friends.extend(lucky_numbers)
print(friends)

#Using insert function/adds a new data to the list by specified index location
friends.insert(1, "Creed")
print(friends)

#Using remove function/removes a data from the list
friends.remove("Johnny")
print(friends)

#Using index function/checks the index of certain element from the list
print(friends.index("Zhongli"))

#Using count function/counts the number of times a certain element is from a the list
print(friends.count("Leonard"))

#Using sort function/sort the list into ascending order
lucky_numbers.sort()
print(lucky_numbers)

#Using reverse function/sort the list into descending order
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

#Using pop function/removes the last element from the list
friends.pop()
print(friends)

#Using clear function/clears all the data from the list
friends.clear()
print(friends)
