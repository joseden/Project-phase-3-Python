#!/usr/bin/env python3
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///banking_system.db')
    Session = sessionmaker(bind=engine)
    session = Session()

import ipdb; ipdb.set_trace()


    
    
    