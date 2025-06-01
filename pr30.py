# sys.exit

import sys

if len(sys.argv)<2:
    sys.exit("Too few argument")
elif len(sys.argv)>2:
    sys.exit("Too many arguments")
print("Hello, My name is",sys.argv[1])
