#Find both half of the programs from the other two repositories and connect them together to make a program

#WAP to print the largest number between 3 using if

n1 = int(input("enter the first number: "))
n2 = int(input("enter the second number: "))
n3 = int(input("enter the third number: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} is the largest")
elif n2 > n1 and n2 > n3:
    print(f"{n2} is the largest")
else:
    print(f"{n3} is the largest")
