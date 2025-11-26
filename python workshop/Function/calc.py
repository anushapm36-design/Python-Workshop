def userInput():
    first_input=int(input("Enter the first number"))
    first_input=nt(input("Enter the second number"))
    return first_input,second_input

def add(a=0,b=0):
    return a+b

def sub(a=0,b=0):
    return a-b

def multiply(a=0,b=0):
    return a*b
print("welcome")
while True:
    print("select the choice:\n 1:add \n 2:sub\n 3:multiply\n 4:stop")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        x,y=userInput()
        print(f"Addition of two numbers: {add(x,y)}")
    elif(choice==2):
        x,y=userInput()
        print(f"Subtraction of two numbers:{sub(x,y)}")
    elif(choice==3):
        x, y=userInput()
        print(f"multiplication of two numbers:{multiply(x,y)}")
    elif(choice==4)
        break
    else:
        print("end")

