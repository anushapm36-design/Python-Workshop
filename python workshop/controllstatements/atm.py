balance=1000
type=(input("enter credit or debit"))
    if(type=="credit"):
       credit_amount=int(input("Enter credit amount"))
       balance+=credit_amount;
       print(f"the current balance is:{balance}")
       elif(type=="debit"):
           (debit_amount)=int(input("enter the debit amount"))
       if(balance<debit_amount):
          balance=balance-debit_amount
          print("amount debit and current balance is{balance}")
    else:
        print("insuffient  balance")


