import math
print("Choose the trignometric function you want to perform.")
print("1. sin")
print("1. cos")
print("1. tan")
option=input("Enter the number of the function you want to perform: ")
if option=="1":
    ans= int(input("Enter the number: "))
    value= math.sin(ans)
    print(value)
elif option== "2":    
    ans= int(input("Enter the number: "))
    value= math.cos(ans)
    print(value)
elif option== "3":    
    ans= int(input("Enter the number: "))
    value= math.tan(ans)
    print(value)
else:
    print("\nInvalid function number!!")    