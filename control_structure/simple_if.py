# syntax 
# if condition: 
#     //code
age =int(input("Enter your age: "))  # takes input from the user and assigns it to the variable 'age'
if age >= 18:  # checks if the age is greater than or equal to 18
 print("You are eligible to vote.")  # executes this block if the condition is true

 # condition is false, nothing will be printed 

 # Mu;ltiple statements can be executed in the if block by using indentation. For example:
if age >= 18:  # checks if the age is greater than or equal to 18
    print("You are eligible to vote.")  # executes this block if the condition is true
    print("You can also apply for a driving license.")  # executes this block if the condition is true
print("This statement is outside the if block and will always be executed.")  # this statement is outside the if block and will always be executed

# ATM example
balance = 1000  # initial balance
withdraw_amount = int(input("Enter the amount to withdraw: "))  # takes input from the user for withdrawal amount
if withdraw_amount <= balance:  # checks if the withdrawal amount is less than or equal to the balance
    balance -= withdraw_amount  # deducts the withdrawal amount from the balance
    print(f"Withdrawal successful. Your new balance is: {balance}")  # prints the new balance      


# attendance example
