
# r stands for read
die_roller_file = open("Die.txt", "r")

# readable checks whether if the file can be read or not
#print(die_roller_file.readable())

# displays the content of the file
#print(die_roller_file.read())

# displays the first line of the file
#print(die_roller_file.readline())

# displays the content of the file in lists format
#print(die_roller_file.readlines())

die_roller_file.close()


# w stands for write
#open("Die.txt", "w")

# a stands for append
#open("Die.txt", "w")

# r+ stands for read and write
#open("Die.txt", "r+")