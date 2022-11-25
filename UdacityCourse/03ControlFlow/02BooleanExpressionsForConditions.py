# USING TRUTH VALUES OF OBJECTS
points = 174  # use this as input for your submission

# Establish the default prize value to None
prize = None

# Use the points value to assign prizes to the correct prize names
if points <= 50:
    prize = "wooden rabbit"
    result = "Congratulations! You won a {}!.".format(prize)
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    prize = "wafer thin mint"
    result = "Congratulations! You won a {}!".format(prize)
else:
    prize = "penguin"
    result = "Congratulations! You won a {}!".format(prize)

print(result)

# or

points = 174 
prize = None

if points <= 50:
    prize = "wooden rabbit"
elif 150 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 180:
    prize = "penguin"

# Use the truth value of prize to assign result to the correct message
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)
