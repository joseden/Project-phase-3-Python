
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

# Create the SQLAlchemy engine for the main database
main_engine = create_engine('sqlite:///banking_system.db')

# Create a session maker bound to the engine
Session = sessionmaker(bind=main_engine)
