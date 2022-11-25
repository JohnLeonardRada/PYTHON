horoscopes = {
    "Aquarius": "You're Lucky Today!",
    "Pisces": "You're Lucky Today!",
    "Aries": "You're Lucky Today!",
    "Taurus": "You're Lucky Today!",
    "Gemini": "You're Lucky Today!",
    "Cancer": "You're Lucky Today!",
    "Leo": "You're Lucky Today!",
    "Virgo": "You're Lucky Today!",
    "Libra": "You're Lucky Today!",
    "Scorpio": "You're Lucky Today!",
    "Sagittarius": "You're Lucky Today!",
    "Capricorn": "You're Lucky Today!"
}
sign = input("What's your horoscope: ")

if sign in horoscopes:
    signs  =  horoscopes[sign]
    print(signs.capitalize())
else:
    print("Unknown Sign!")
