# WHICH PRIZE
# TODO: Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points
# Points	Prize
# 1 - 50	wooden rabbit
# 51 - 150	no prize
# 151 - 180	wafer-thin mint
# 181 - 200	penguin

points = 174  # use this input to make your submission

if points <= 50:
    result = "Congratulations! You won a wooden rabbit."
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint."
else:
    result = "Congratulations! You won a penguin."

print(result)

# GUESS MY NUMBER
# '''
# You decide you want to play a game where you are hiding
# a number from someone.  Store this number in a variable
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''

answer = 50
guess = 25

if guess < answer:
    result = "Oops! Your guess was too low."
elif guess > answer:
    result = "Oops! Your answer was too high."
elif guess == answer:
    result = "Nice! Your guess matched the answer."

print(result)

# TAX PURCHASE
# '''
# Depending on where an individual is from we need to tax them
# appropriately.  The states of CA, MN, and
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and
# the corresponding state to assure that they are taxed by the right
# amount.
# '''

state = "NY"
purchase_amount = 1000

if state == "CA":
    tax_amount = 0.075
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)
elif state == "MN":
    tax_amount = 0.095
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)
elif state == "NY":
    tax_amount = 0.089
    total_cost = purchase_amount * (1 + tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)