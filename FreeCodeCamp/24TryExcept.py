
try:
    #answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by Zero")
#Printing the default message of that exception
#except ZeroDivisionError as err:
#   print(err)
except ValueError:
    print("Invalid Input!")