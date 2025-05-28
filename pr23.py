#Exceptions part2:
#With using 'pass'

def main():
    x = get_int() 
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass

main()