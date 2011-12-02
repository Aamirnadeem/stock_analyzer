#!/usr/bin/python
import argparse, MySQLdb
import matplotlib.pyplot as stock_plot
from symbol import *
import database_classes

def main():
    print_welcome_message()
    results = parse_args()
    render_chart(results)

def print_welcome_message():
    print "Welcome to Charty stock chart viewing utility"

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', action='store', dest='symbol', help='Specify which symbol you would like to chart', required=True)
    return parser.parse_args()


def render_chart(results):
    #x = 31 for days in month
    x = 31
    low = get_52_week_low(results.symbol)
    high = get_52_week_high(results.symbol)
    y = (low,high)
    days = []
    for x in range(1,19):
        y = 0
        y = x + 0.0
        days.append(y)
        

    start_date = '20111001'
    end_date = '20111030'
    prices = get_historical_prices(results.symbol,start_date,end_date)
    prices = prices[1:]
    opens = []
    for price_array in prices:
        y = float(price_array[1])
        opens.append(y)
    print opens
    print days
    #a = stock_plot.plot(x,y)
    b = stock_plot.plot(days, opens, 'go-', label='line 1', linewidth=2)
    stock_plot.show()
main()
