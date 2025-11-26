balance=10000
amount=int(input("enter your amount"))
if(amount>balance):
    print("insufficient balance")
else:
    print("your amount has been debited")
    balance-=amount
    print(f"new balance{balance}")

