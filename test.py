import num2words

print("Convert number to word")
try:
    a = int(input("Enter number: "))
    b = num2words.num2words(a)
    print(b)
except ValueError:
    print("Please enter a valid number")