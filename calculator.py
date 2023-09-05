def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y == 0:
        print("Error: Cannot divide by zero.")
        return
    return x/y

def mod(x,y):
    return x%y
i=1

while(i==1):
    print("Select the desired operation : ")
    print("1 for addition.")
    print("2 for subtraction.")
    print("3 for multiplication.")
    print("4 for division.")
    print("5 for modulus.")
    
    choice=input()


    if choice in ("1","2","3","4","5"):
        try:
            no1=int(input("Enter the first operand : "))
            no2=int(input("Enter the second operand : "))
    
        except ValueError:
            print("Invalid Input, please enter a value which is valid.") 
    
        if choice=="1":
            print(no1,"+",no2," = ",add(no1,no2))
        elif choice=="2":
            print(no1,"-",no2," = ",sub(no1,no2))
        elif choice=="3":
            print(no1,"*",no2," = ",mul(no1,no2))
        elif choice=="4":
            print(no1,"/",no2," = ",div(no1,no2))
        elif choice=="5":
            print(no1,"%",no2," = ",mod(no1,no2))
    else:
        print("Invalid choice. Please enter a valid option.")
    i=int(input("Do you want to continue?If yes enter 1 else enter 2 : "))
