"""
Kaveh Masoudinia
section 2 exercise 3
"""
n1=0
n2=1
count=0
number = int(input("enter a number:"))
while count<number:
    n3=n1+n2
    n1 = n2
    n2 = n3
    count += 1
print(n1)