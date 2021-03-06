#!/usr/bin/python

from symbol import *
import datetime
import MySQLdb
import re

conn = MySQLdb.connect('localhost','root','jonjon','stock_history')
cursor = conn.cursor()

def get_now():
    return datetime.datetime.now()

def add_stock(symbol):
    price = get_price(symbol)
    query = query_builder('insert','price_history',[symbol,price,get_now()])    
    cursor.execute(query)

def watch_stock(symbol):
    price = get_price(symbol)
    query = query_builder('insert','stock_watch',[symbol,price,get_now()])
    cursor.execute(query)

def query_builder(qtype,table,values=''):
    if(qtype == 'insert'):
        query = "insert into "
        query += table
        query += " values('"
        for value in values:
            query += str(value) + "','"
        query = query[0:-2]
        query += ");"
        #print "the query is: " + query
        return query
    if(qtype == 'select all'):
        query = "select * from "
        query += table
        query += ";"
        #print query
        return query

def get_watched_stocks():
    query = query_builder('select all','stock_watch')
    cursor.execute(query)
    row = cursor.fetchall()
    print_rows(row)
def print_rows(rows):
    for row in rows:
        print row

def import_stock_list(list_name):
    symbol = open(list_name, 'r')
    lines = symbol.readlines()
    
    symbol_only = []
    for line in lines:
        first = re.split('\t|\r|\n',line)
        symbol_only.append(first[0])

    for symbol in symbol_only:
        add_stock(symbol)
        
def get_favorite_stocks():
    favorite_stocks = ['KV.A','DELL','AAPL','MSFT']
    return favorite_stocks

#commands for the stock analyzer system
#######################################
##Configure Commnads Below
#
#watch a stock
#watch_stock('MSFT')
#
#add a stock
#add_stock('MSFT')
#get_watched_stocks();
#import_stock_list('NYSE.txt')

conn.close()
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D #<-- Note the capitalization! 
fig = plt.figure()

ax = Axes3D(fig) #<-- Note the difference from your original code...

X, Y, Z = axes3d.get_test_data(0.05)
cset = ax.contour(X, Y, Z, 16, extend3d=True)
ax.clabel(cset, fontsize=9, inline=1)
plt.show()
