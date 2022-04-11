"""
Kaveh Masoudinia
section 2 exercise 5
"""
total=0
n1 = 0
number=input("Enter a number:")
x=len(number)
for i in range(x):
    a=int(number)%10
    number=int(number)/10
    n2 = (2 ** n1)*a
    total=total+n2
    n1+=1
print(total)
