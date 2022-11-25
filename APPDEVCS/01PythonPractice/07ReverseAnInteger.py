number = (input("Enter any number: "))

reversed_number = number[::-1]

try:
    changed_to_int = int(reversed_number)
    print(changed_to_int)
except ValueError:
    print(f"[ERROR] {number} was an invalid integer input.")