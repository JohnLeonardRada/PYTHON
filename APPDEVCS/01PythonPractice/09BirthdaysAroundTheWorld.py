greetings = {
    "English": "Happy Birthday, ",
    "Japanese": "Oo Tanjobi Omedetou, ",
    "Filipino": "Maligayang Kaarawan, ",
    "Chinese": "Shēng Rì Kuài Lè, ",
}

name = input("What's your name?: ")
language = input("What language are you using?: ")

if language in greetings:
    print(greetings[language] + name)
else:
    print(f"Happy Birthday, {name}")


# or using handler

def japanese(name):
    return f"Tanjobi Omedetou, {name}-san"

def english(name):
    return f"Happy Birthday, {name}"

def main():
    name = input("What's your name?: ")
    language = input("What language are you using?: ")
    
    greeters = {"Japanese": japanese, "English": english}
    default_greeter = greeters["English"]
    greeter = greeters.get(language, default_greeter)
    greeting = greeter(name)
    print(greeting)

if __name__ == '__main__':
    main()