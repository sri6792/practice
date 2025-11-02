a = int(input("enter 1 number: "))
b = int(input("enter 2nd number: "))
for i in range(1,6):
    for j in range(1,6):
        print("1. ADD")
        print("2. SUBTRACT")
        print("3. MULTIPLICATION")
        print("4. DIVISION")
        choice=int(input("enter your choice: "))
        if choice==1:
           c=a+b
           print("sum of 2 numbers is",c)
           break
        elif choice==2:
           c = a-b
           print("subtraction of 2 numbers is",c)
           break
        elif choice == 3:
           c = a*b
           print("multiplication of 2 numbers is",c)
           break
        elif choice == 4:
            if b!=0:
               c = a/b
               print("division of 2 numbers is",c)
               break
        else:
            print("wrong choice")

