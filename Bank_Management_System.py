class BankAccount:
    def __init__(self, name , branch , amount):
        self.name = name
        self.branch = branch 
        self.amount = amount
    def display_balance(self):
        print("\nAccount Holder" , self.name)
        print("Branch: ", self.branch)
        print("Current Balance: ₹" , self.amount)
    def deposit(self,money):
            if money > 0:
                self.amount = self.amount + money
                print("Money deposited successfully")
                print("New Balance: ₹" , self.amount)
            else:
                print("Enter a valid amount")
    def withdraw(self, money):
            if money < self.amount:
                self.amount = self.amount - money
                print("Remaining Balance: ₹", self.amount)
            else:
                print("Insufficient Balance")
        
s1 = BankAccount("Yafis" , "Residency Road" , 5000000)
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
    
