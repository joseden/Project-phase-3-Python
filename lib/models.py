# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    balance = Column(Numeric(10, 2))
    password = Column(String)
    deposits = relationship("Deposit", backref="account")
    withdrawals = relationship("Withdrawal", backref="account")

class Deposit(Base):
    __tablename__ = 'deposits'

    deposit_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    amount = Column(Numeric(10, 2))
    timestamp = Column(DateTime, default=func.now())

class Withdrawal(Base):
    __tablename__ = 'withdrawals'

    withdrawal_id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    amount = Column(Numeric(10, 2))
    timestamp = Column(DateTime, default=func.now())
