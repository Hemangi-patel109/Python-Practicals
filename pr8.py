name = input("What's your name? ")
name = name.strip()
print(name)
name = name.capitalize()
print(name)
name = name.strip().title()
print(name)

#Or all 7 line code in one line:

name = input("What's your name? ").strip().title()
print(name)