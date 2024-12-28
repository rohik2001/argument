#create an acoount with an initial balance
def create_account (name, initial_balance):
    print (f"account created successfully for {name} with balance {initial_balance}")
    return initial_balance
# deposit money into account
def deposit(balance,amount):
    balance=balance+amount
    print(f"diposited: {amount}. current balance : {balance}")
    return balance
def withdraw(balance,amount):
    if amount>balance:
        print("insufitiant balance")
    else:
        balance=balance-amount
        print(f"withdraw: {amount}. current balance: {balance}")
        return balance
def trancefer(sender_balance,recever_balance,amount):
    if amount>sender_balance:
        print("insuufitiant Balance")
    else:
        sender_balance=sender_balance-amount
        recever_balance=recever_balance+amount
        print(f"Transferred: {amount}. Sender's balance is: {sender_balance}. receiver balance:{receiver_balance}")
        return sender_balance, receiver_balance


def check_balance(balance):
    print(f"current balance : {balance}")
    return balance

balance=create_account("Rohik",5000)
balance=deposit(balance,110)
balance=withdraw(balance,1100)
balance=check_balance(balance)
sender_balance=2000

receiver_balance=3000

sender_balance,receiver_balace=trancefer(sender_balance, receiver_balance,300)