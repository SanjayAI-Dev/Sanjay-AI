
'''
list
name=['ravi','sai','kiran']
print(len(name))
print(name[2])'''

'''fruits=('apple','banana','kiwi','apple')
print(len(fruits))
print(type(fruits))'''

num=[1,2,3,4,5]
num.append(10)
print(num)

num.extend([6,7,8,9])
num.append(21)
print(num)
num.insert(7,3)
print(num)
#num.remove(3)
num.remove(5)
print(num)
#num.clear()
#print(num)
print(num.index(6))
print(num.count(3))
#print(num.sort())
num.sort()
print(num)
num.reverse()
print(num)
num.reverse()
print(num)
a=num.copy()
print(a)

#list operations 

print(20 in a)
print(100 not in a)

b=a+[40+30]
print(b)
c=b*2
print(c)
c.sort()
print(c)
num.pop()
print(num)
