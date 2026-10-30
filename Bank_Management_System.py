class BankAccount:
    min_balance = 1000
    def __init__(self, name , branch , phone, amount):
        self.name = name
        self.branch = branch 
        self.phone = phone
        self.amount = amount
        self.send_sms(f"Welcome to {self.branch} Branch , Your account is now active")
    def send_sms(self, message):
            print(f"\n [SMS ALERT to {self.phone}]: Dear {self.name} , {message} Avl Bal: {self.amount}")
    def display_balance(self):
        print("\nAccount Holder" , self.name)
        print("Branch: ", self.branch)
        print("Registered Mobile", self.phone)
        print("Current Balance: ₹" , self.amount)
    def deposit(self,money):
            if money > 0:
                self.amount = self.amount + money
                print("Money deposited successfully")
                self.send_sms(f"Dear {self.name} , {money} has been credited to you Bank Account")
                print("New Balance: ₹" , self.amount)
            else:
                print("Enter a valid amount")
    def withdraw(self, money):
            if money <= 0:
                print("Enter a valid amount")
            elif self.amount - money < BankAccount.min_balance:
                print(f"Transaction delined! You must maintain a minimum balance of {BankAccount.min_balance}")
                self.send_sms(f"Dear costumer {self.name}, Withdrawl of {money} has been declined due to insuffiect balance")
            else:
                self.amount = self.amount - money
                print("Withdrawl Successfull")
                print("Remaining Balance ₹, self.amount")
                self.send_sms(f"Dear costumer {self.name}, Amount of {money} has been debited from your Bank Account")  
                
                      
print("--Open a New Bank Account--")
name = input("Enter Account Holder Name: ")
branch = input("Enter the Branch name: ")
phone = input("Enter the Mobile Number for SMS Alert: ")


while True:
    initial_amount = float(input(f"Enter The initial deposit , Initial deposit must be at least {BankAccount.min_balance}: "))
    if initial_amount >= BankAccount.min_balance:
        s1 = BankAccount(name , branch , phone , initial_amount)
        break
    else:
        print(f"Account cannot be opened! Initial balance must be at least {BankAccount.min_balance}")
while True:
    print("\n ---Bank Details Menu---")
    print("1. Display Account Details")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        s1.display_balance()
    elif choice == "2":
        print("Current Balance: ₹" , s1.amount)
    elif choice == "3":
        money = float(input("Enter the amount to deposit: ₹"))
        s1.deposit(money)
    elif choice == "4":
        money = float(input("Enter the money to withdraw: ₹"))
        s1.withdraw(money)
    elif choice == "5":
        print("Thank You for using your bank server")
        break
    else:
        print("Invalid choice. Please try again")
    
