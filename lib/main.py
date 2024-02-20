#!/usr/bin/env python

import random
from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from decimal import Decimal
from models import Base, Account, Deposit, Withdrawal

fake = Faker()

engine = create_engine('sqlite:///banking_system.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def generate_fake_data(session):
    # Generate fake accounts
    for _ in range(20):
        account = Account(
            name=fake.unique.name(),
            balance=random.randint(10, 10000),
            password=fake.password()
        )
        session.add(account)

    # Generate fake deposits and withdrawals
    accounts = session.query(Account).all()
    for account in accounts:
        for _ in range(random.randint(1, 5)):
            deposit = Deposit(
                account_id=account.id,
                amount=random.randint(10, 10000)
            )
            session.add(deposit)
            withdrawal = Withdrawal(
                account_id=account.id,
                amount=random.randint(10, 1000)
            )
            session.add(withdrawal)
    session.commit()

def show_menu():
    print("Welcome to the Banking System CLI")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def check_balance(session, account_id):
    account = session.query(Account).filter_by(id=account_id).first()
    if account:
        print(f"Current balance for account {account_id}: ${account.balance}")
    else:
        print("Account not found")

def deposit(session, account_id, amount):
    account = session.query(Account).filter_by(id=account_id).first()
    if account:
        if amount > 0:
            amount = Decimal(amount)
            deposit = Deposit(account_id=account_id, amount=amount)
            account.balance += amount
            session.add(deposit)
            session.commit()
            print(f"Deposited ${amount} into account {account_id}. New balance: ${account.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive number.")
    else:
        print("Account not found")

def withdraw(session, account_id, amount):
    account = session.query(Account).filter_by(id=account_id).first()
    if account:
        amount = Decimal(amount)
        if amount > 0 and account.balance >= amount:
            withdrawal = Withdrawal(account_id=account_id, amount=amount)
            account.balance -= amount
            session.add(withdrawal)
            session.commit()
            print(f"Withdrew ${amount} from account {account_id}. New balance: ${account.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive number.")
        else:
            print("Insufficient funds")
    else:
        print("Account not found")

def main():
    session = Session()
    generate_fake_data(session)

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                account_id = int(input("Enter account ID: "))
                check_balance(session, account_id)
            except ValueError:
                print("Invalid account ID. Please enter a valid integer.")
        elif choice == '2':
            try:
                account_id = int(input("Enter account ID: "))
                amount = float(input("Enter deposit amount: "))
                deposit(session, account_id, amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            try:
                account_id = int(input("Enter account ID: "))
                amount = float(input("Enter withdrawal amount: "))
                withdraw(session, account_id, amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()