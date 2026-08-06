"""#condition statement
#if stmt
age=20
has_id=True
if age>18 and has_id:
    print(age)
else:
    print()
   

'''num=int(input("enter your number"))
if num%2==0:
    print("its even number")
else:
    print("its odd number")'''

#if-else   else-if
'''marks = int(input("enter your student marks"))
if marks >= 90:
    print("Grade A")
elif marks >=70:
    print("Grade B")
elif marks >= 60:
    print("grade C")
else:
    print("Fail")
"""

# loop concept  
#  2  types of loop in python 
#1.for loop(list , tuples , string and range-->limited values)
#2.while loop(unlimited values)

'''i=2
for i in range(2,5):
    print(i)

'''
'''for n in range(1,11):
    print(f"2 * {n} = {2 * n }")

'''
#while loop
'''a=1
while a <= 90:
    a+=3
    print(a)
   
'''
#3types of loops
#1.break-stops the loop immediately
#2.continue-skip the current loop to the next
#3.pass-help to expect the stmt..

'''a=1
while a<=100:
    if a==50:
        break
    print(a)

    a+=1'''
'''a=1
while a<=100:
    if a==50:
        continue
    print(a)

    a+=1'''

a=1
while a<=100:
    if a==50:
        pass
    print(a)

    a+=1

