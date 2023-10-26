#2.1 lmplement a class called bankaccount that represents a bank account. the class should have private attributes for account number, account holder name,and account balance.lnclude methods to deposit money,withdraw money,and display the account balance.ensure that the account balance cannot be accessed directly from outside the class.write a program to create an instance of the bank account class and test the deposit and withdrawal functionality.
class bankaccount:
  def __init__(self, account_number, account_holder_name,  initial_balance=0.0):
   self.__account_number = account_number
   self.__account_holder_name = account_holder_name
   self.__account_balance = initial_balance
    
  def deposit(self,amount):
    if amount > 0:
     self.__account_balance+= amount
     print(f"Deposited ${amount:.2f} into account {self.__account_number}")
    else:
     print("invalid deposit amount. please deposit a positive amount.")

  def withdraw(self,amount):
    if amount > 0:
     if self.__account_balance >= amount:
       self.__account_balance -= amount
       print(f"deposit ed${amount:2f} from account {self.__account_number}")
    else:
       print("lnvaid deposit amount.please deposit a positive amount.")
      
  def display_balance(self):
     print(f"account {self.__account_number} balance: ${self.__account_balance:2f}")

#testing the bankaccount class
  if_name_="__main__"
  #create a bank account instance
account1 = bankaccount("123456","John Doe", 1000.0)
#deposit money 
account1.deposit(500.0)
#withdraw money
account1.withdraw(200.0)
#display balance
account1.display_balance()
    


      



