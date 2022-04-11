"""
Kaveh Masoudinia
section 2 exercise 4
"""
n=0
print("Shape A")
for i in range(n,11):
    print(n*'*')
    n+=1
print()
n=10
print("Shape B")
for j in range(n,0,-1):
    print(n*'*')
    n-=1
print()
n=10
z=1
print("Shape C")
for j in range(n,0,-1):
    print(n*'*','\n',end=z*' ')
    n-=1
    z+=1
print()
n=1
z=10
print("Shape D")
for j in range(0,z):
    print(z*' ',n*'*')
    n+=1
    z-=1