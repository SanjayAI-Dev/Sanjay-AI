"""
Accepts the user's name.
Accepts the user's age.
Accepts the user's city.
Calculates the year in which the user will turn 100 (assume the current year is 2026).
Displays the information using f-strings.

"""

name=input("whats your name : ")
age=int(input("Whats your age: "))
city=input("enter your city: ")
c=100-age
d=2026+c
print(f"Welcome {name}")
print(f"your age is {age}")
print(f"you will be 100 in ",{d})
print(f"you will be 100 in : ",{100-age})
print(f"you live in {city}")



