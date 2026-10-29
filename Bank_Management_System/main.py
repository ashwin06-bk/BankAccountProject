class BankAccount:
  def __init__(self,account_holder,account_number,balance):
    self.account_holder = account_holder
    self.account_number = account_number
    self.balance = balance

 
  def display_details(self):
    print("\nAccount Created successfuly")
    print("Account Holder:",self.account_holder)
    print("Account Number:",self.account_number)
    print("Balance:",self.balance)

print("\nWelcome to Rspace Bank")
print("1.Create New Account")
print("2.Deposit Money")
print("3.Withdraw Money")
print("4.Check balance")
print("5.View Account Details")
print("6.Exit")



try:
    choice = int(input("Enter Your Choice(1-6):"))

    if choice ==1:
      account_holder = str(input("Enter Customer Name: "))
      account_number = int(input("Enter Account Number: "))

      try:
        balance = float(input("Enter Account Opening Amount: "))

        if balance<0:
          print("Enter Positive Number!")

        else:
          account =BankAccount(account_holder,account_number,balance)
          account.display_details()

      except ValueError:
        print("Invalid Input! Please Enter valid Amount.")
      
      
    

    elif choice ==2:
      print("2.Deposit Money")

    elif choice ==3:
      print("3.Withdraw Money")

    elif choice ==4:
      print("4.Check Balance")

    elif choice == 5:
      print("5.View Account Details")

    elif choice == 6:
      print("Thank you for banking with Rspace Bank")

    else:
      print("Choose Correct option")
except ValueError:
  print("Invalid Input ! Enter a Number")





account_holder = input("Enter Customer Name: ")
account_number = input("Enter Account Number: ")
balance = float(input("Enter account opening amount: "))










