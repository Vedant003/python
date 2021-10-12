# Program to make simple calculator
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def Multiply(x,y):
    return x * y
def Divide(x,y):
    return x / y    

print("Select operations")
print("1.Add")
print("2.subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice (1,2,3,4): ")
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(num1, "+",num2, "=",add(num1,num2))
        elif choice == '2':
            print(num1, "-",num2, "=",subtract(num1,num2))
        elif choice == '3':
            print(num1, "*",num2, "=",Multiply(num1,num2))
        elif choice == '4':
             print(num1, "/",num2, "=",Divide(num1,num2))
        break
    else:
        print("invalid input !!!")
                        

                    
                