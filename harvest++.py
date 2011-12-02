import MySQLdb,datetime,re,argparse
from symbol import *
import database_classes

def main():
    print_welcome_message()
    results = parse_args()
    pull_stocks(results)
def print_welcome_message():
    print "Welcome to Stock Harvester"

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', action='store',dest='exchange',help='Specify which exchange you would like to harvest',required=True)
    return parser.parse_args()
    

def pull_stocks(results):
    if(results.exchange == 'nyse'):import_stock_list('NYSE.txt')

def import_stock_list(list_name):
    symbol = open(list_name, 'r')
    lines = symbol.readlines()

    symbol_only = []
    for line in lines:
        first = re.split('\t|\r|\n',line)
        symbol_only.append(first[0])
    progress_count = 0.0
    for symbol in symbol_only:
        add_stock(symbol)
        print "percentage finished:  \n"
        progress =  progress_count / len(symbol_only)
        print progress
        
        print "Adding:"
        print symbol
        progress_count += 1

def add_stock(symbol):
    price = get_price(symbol)
    eps = get_earnings_per_share(symbol)
    print price , "\n"
    print "Eps: ",eps
    print "\n"
    stock = database_classes.Stock(symbol,price,datetime.datetime.now(),eps)
    database_classes.session.add(stock)
    database_classes.session.commit()

main()
