"""
Kaveh Masoudinia
section 2 exercise 2
"""
total=0
counter=0
E_day=[]
Number_Day=int(input("How many days do you want to enter?"))
for i in range(0,Number_Day):
    days=int(input())
    E_day.append(days)
    total+=days
    i+=1

print("Total:",total)
print("Max:",max(E_day))
print("Min:",min(E_day))
print("Average:",total/Number_Day)