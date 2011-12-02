#!/usr/bin/env=python
import MySQLdb,datetime,re,argparse
from symbol import *
import database_classes
from sqlalchemy.sql import select
from datetime import date

def main():
    print_welcome_message()
    results = parse_args()
    analyze_multiple(results)
def print_welcome_message():
    print "Welcome to the Stock Analyzer"

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', action='store',dest='exchange',help='Specify which exchange you would like to harvest',required=True)
    return parser.parse_args()

def analyze_multiple(results):
    if(results.exchange == 'nyse'): pull_symbols('NYSE.txt')

def pull_symbols(symbol_list):
    symbol = open(symbol_list, 'r')
    lines = symbol.readlines()
    symbol_only = []
    for line in lines:
        first = re.split('\t|\r|\n',line)
        symbol_only.append(first[0])
    progress_count = 0.0
    for symbol in symbol_only:
        #calculate_multiple(symbol)
        progress =  progress_count / len(symbol_only)
        print "percentage finished: ", progress
        print "Calculating Multiples: ", symbol
        calculate_multiple(symbol)
        progress_count += 1

def calculate_multiple(symbol):
    file_name = 'dead_list ' + str(date.today()) + '.txt'
    deadlist = open(file_name, 'a' )
    
    result_list = []
    call_sign = symbol
    conn = database_classes.engine.connect()
    s = select([database_classes.Stock.call_sign,database_classes.Stock.price,database_classes.Stock.eps], database_classes.Stock.call_sign.like(symbol)) 
     
    result = conn.execute(s)
    #turn result object into list
    for row in result:
        result_list.append(row)
    current_info = result_list[-1]
    price = current_info[1]
    eps = current_info[2]
    
    print "PRICE : ",price,"EPS: ",eps, "P/E RATIO: "
    if(eps != 0): 
        multiple = price/eps 
    else: 
        print "EPS == ZERO"

    if(eps < 0):
        print "adding stock to deadlist"
        deadlist.write('%s %s %s \n' % (symbol,price,eps))
        
    

main()
