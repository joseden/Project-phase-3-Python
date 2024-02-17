from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Account,Deposit,Withdrawal

if __name__ == '__main__': 
    # Create SQLAlchemy engine
    engine = create_engine('sqlite:///banking_system.db')
    
    # Bind the engine to a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Initialize Faker to generate fake data
    fake = Faker()

    # Generate fake data for accounts
    for _ in range(10):
        account = Account(
            name=fake.unique.name(),
            balance=random.randint(100, 10000),
            password=fake.password()
        )
        session.add(account)

    # Commit the added accounts
    session.commit()
    
    # Generate fake data for deposits
    accounts = session.query(Account).all()
    for account in accounts:
        for _ in range(random.randint(1, 5)):
            deposit = Deposit(
                account_id=account.id,
                amount=random.randint(10, 1000)
            )
            session.add(deposit)

    # Commit the added deposits
    session.commit()
    
    
      # Generate fake data for withdrawals
    for account in accounts:
        for _ in range(random.randint(1, 5)):
            withdrawal = Withdrawal(
                account_id=account.id,
                amount=random.randint(10, 500)
            )
            session.add(withdrawal)

    # Commit the added withdrawals
    session.commit()

    # Close the session
    session.close()
    
    