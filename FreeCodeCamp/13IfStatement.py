
is_male = False
is_tall = True

if is_male:
    print("You are a male")

if is_male or is_tall:
    print("You are a male")
else:
    print("You are not male")

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are not a male and not tall")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not male but are tall")
else:
    print("You are not a male and not tall")

