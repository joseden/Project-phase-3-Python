# db/models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

Base = declarative_base()
engine = create_engine('sqlite:///banking_system.db')
Session = sessionmaker(bind=engine)
session = Session()

class Account(Base):
    __tablename__ = 'accounts'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    balance = Column(Numeric(10, 2))
    password = Column(String)
    
    def __repr__(self):
        return f'Account(id={self.id}, ' + \
            f'name={self.name}, ' + \
            f'balance={self.balance})'


class Deposit(Base):
    __tablename__ = 'deposits'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    amount = Column(Numeric(10, 2))
    timestamp = Column(DateTime, default=func.now())
    
    def __repr__(self):
        return f'Deposit(id={self.id}, ' + \
            f'name={self.account_id}, ' + \
            f'balance={self.amount})'
        
class Withdrawal(Base):
    __tablename__ = 'withdrawals'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    amount = Column(Numeric(10, 2))
    timestamp = Column(DateTime, default=func.now())
    
    def __repr__(self):
        return f'Deposit(id={self.id}, ' + \
            f'name={self.account_id}, ' + \
            f'balance={self.amount})'
            

Account.deposits = relationship("Deposit", backref="account")
Account.withdrawals = relationship("Withdrawal", backref="account")


Base.metadata.create_all(engine)

 
 
 


