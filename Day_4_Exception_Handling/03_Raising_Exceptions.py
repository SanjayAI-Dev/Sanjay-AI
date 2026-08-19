"""# 03_Raising_Exceptions
try:
    age = int(input("enter your age"))

    if age < 18:
        raise ValueError(                   #specifies specify the error manually
            "You must be 18 or older."
        )

except ValueError as e:                     #prints the object

    print(e)



#custom exception

"""
class InvalidAgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise InvalidAgeError("You must be 18 or older")

    print("You are eligible")

except InvalidAgeError as e:
    print("Error:", e)