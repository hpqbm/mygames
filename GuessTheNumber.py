
import math
import random

num = random.randint(1,100)

print("""Hello! I am thinking of a random number between 1 and 100!Try and guess it!
I will tell you if the number is greater than or less than the number I am thinking about. So, give a first guess:""")
i = int(input(""))
tries = 1
while i != num:
    if i < num:
        print(f"The number I am thinking of greater than {i}")

    if i > num:
        print(f"The number I am thinking of less than {i}")
    i = int(input(""))
    tries += 1

print(f"You got it! It is {num}! You took {tries} tries ")


