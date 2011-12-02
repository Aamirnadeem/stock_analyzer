#!/usr/bin/python
from sqlalchemy import *
from base_class import *
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_engine('mysql+mysqldb://root:jonjon@localhost/stock_history')
Session = sessionmaker(bind=engine)

class Stock(Base):
    __tablename__ = 'Stocks'

    call_sign = Column(String(10), primary_key=True)
    
    price = Column(Float)
    
    date_added = Column(DateTime, primary_key=True)    

    eps = Column(Float)
    def __init__(self,call_sign,price,date_added,eps):
        self.call_sign = call_sign
        
        self.price = price
        self.date_added = date_added
        self.eps = eps

    def __repr__(self):
        return "<Stock('%s','%s','%s','%s')>" % (self.call_sign, self.price,self.date_added,self.eps)


Stock.metadata.create_all(engine)
session = Session()




