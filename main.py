#Code conversion project
#najim sultani
#3-18-23
#python
import pickle
import os
class Customer:
  def __init__(self,A):##what happens if you want to make account
    self.name=input("Enter Name: ")#name
    self.type=input("Type of Account s/c?: ")#type
    self.amount=int(input("Enter Amount: "))#amount
    while True:
      if self.type=='s':##type
        if self.amount<5000:#more than 5,000
          print("Min 5000 required")
          self.amount=int(input("Please Enter amount again: "))##try again
        else:
          break
      if self.type=='c':#type
        if self.amount<2000:##more then 2,000
          print("Min 2000 required")
          self.amount=int(input("Please Enter amount again: "))##try again
        else:
          break
    self.accountNo=A##give you a account number
    print("Your Account No. is:",self.accountNo)

  def Display(self):
    print("{:<15} {:<15} {:<15} {:<15}".format(self.accountNo,self.name,self.type,self.amount))

def createAccount():
  try:##saves record
    file=open('bank.bin','rb')
    while True:
      t=pickle.load(file)
      A=t.accountNo
  except FileNotFoundError as e:
    A=121000##number
  except EOFError as e:
    A=A+1##adds 1 every time
    file.close()
  file=open('bank.bin','ab')
  s=Customer(A)
  pickle.dump(s,file)
  file.close()
  option()

def ViewAllAccount():
  try:##shows all the accounts made
    file=open('bank.bin','rb')#number, name, type, amount
    print("{:<15} {:<15} {:<15} {:<15}".format('Account No.','Name','Type','Amount'))
    while True:
      t=pickle.load(file)
      t.Display()#display 
  except FileNotFoundError as e:
    print("\nThere Are No Record")#no records
  except EOFError as e:
    file.close()
  option()

def Deposit():##add more money 
  file=open('bank.bin','rb')
  file1=open('tmp.bin','wb')
  x=int(input("Enter Bank Account: "))##by using your account number
  try:
    while True:
      t=pickle.load(file)
      if t.accountNo==x:
        cr=int(input("Enter Deposit Amount: "))##amount you want to deposit
        t.amount=t.amount+cr
      pickle.dump(t,file1)
  except:
    pass
  finally:
    file.close()
    file1.close()
  os.remove('bank.bin')
  os.rename('tmp.bin','bank.bin')
  option()

def Withdraw():
  file=open('bank.bin','rb')
  file1=open('tmp.bin','wb')
  x=int(input("Enter Bank Account: "))##take away money 
  try:
    while True:
      t=pickle.load(file)
      if t.accountNo==x:
        dr=int(input("Enter Withdraw Amount: "))##amount
        if t.type=='s':#type of account
          while True:
            if t.amount-dr<5000:#can't go abow 5,000
              print("Saving Account Balance can't be below 5000")
              dr=int(input("Enter Withdraw Amount: "))
            else:
              t.amount=t.amount-dr
              break
        if t.type=='c':
          while True:
            if t.amount-dr<2000:#can't go less than 2,000
              print("Currunt Account Balance can't be below 2000")
              dr=int(input("Enter Withdraw Amount: "))##how muuch
            else:
              t.amount=t.amount-dr
              break
      pickle.dump(t,file1)
  except:
    pass
  finally:
    file.close()
    file1.close()
  os.remove('bank.bin')
  os.rename('tmp.bin','bank.bin')
  option()

def Update():
  file=open('bank.bin','rb')
  file1=open('tmp.bin','wb')#number
  x=int(input("Enter Bank Account: "))
  try:
    while True:
      t=pickle.load(file)
      if t.accountNo==x:#change the account name
        name=input("Update Name: ")
        t.name=name#change
      pickle.dump(t,file1)
  except:
    pass
  finally:
    file.close()
    file1.close()
  os.remove('bank.bin')
  os.rename('tmp.bin','bank.bin')
  option()

def Search():#type
  file=open('bank.bin','rb')
  x=int(input("Enter Bank Account: "))#finds your account by number
  try:
    while True:
      t=pickle.load(file)
      if t.accountNo==x:##list these
        print("\nName:",t.name)
        print("Account Type:",t.type)
        print("Amount:",t.amount)
        print("Account No.:",t.accountNo)
        break
  except:
    pass
  finally:
    file.close()
  option()

def Exit():
  pass

def option():
  print()#list everthing here
  print("What Do You Wanna Do\n1. Create Account\n2. View all Account\n3. Deposit\n4. Withdraw\n5. Update\n6. Search\n7. Exit")
  n=int(input())#type 1
  if n==1:
    createAccount()
  elif n==2:#2
    ViewAllAccount()
  elif n==3:#3
    Deposit()
  elif n==4:#4
    Withdraw()
  elif n==5:#5
    Update()
  elif n==6:#6
    Search()
  elif n==7:#7 
    Exit() #exit out
  else:#8 or more
    print("Invalid option")
    print("Try again")
    option()#try again

s="BANKING APP"
print(s.center(45,'*'))#stars
option()
