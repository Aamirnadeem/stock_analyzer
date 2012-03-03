import MySQLdb,datetime,re,argparse
from symbol import *
from database_classes import *
from time import strftime

def get_time():
    now = datetime.datetime.now()
    return now

def get_time_yesterday(today):
    yesterday = today - datetime.timedelta(days=1)
    return yesterday

def get_current_quote(call_sign):
    now_string = strftime("%Y-%m-%d")
    filter_string = "date_added like '%s" % now_string
    filter_string += "%'"
    for instance in session.query(Stock).filter("call_sign = '%s'" % call_sign).filter("%s" % filter_string):
        print instance.price,instance.call_sign,instance.date_added
        return instance.price
def calculate_growth_rate_online(symbol):
    future_eps = float(get_estimate_eps_next_year(symbol))
    print "future EPS is ",future_eps
    current_eps = float(get_earnings_per_share(symbol))    
    print "current_eps is", current_eps
    delta_eps = future_eps - current_eps
    delta_eps *= 100
    delta_eps /= current_eps
    delta_eps_string = str(delta_eps)
    print "The Growth Rate for %s is %s" % (symbol, delta_eps_string,)

def get_quote_download_dates():
  for instance in session.query(Stock.date_added).distinct():
      print instance.date_added

def print_portfolio():
    get_current_quote('SCCO')
    get_current_quote('KMP')
    get_current_quote('MWE')
    get_current_quote('ENB')

def get_current_eps(symbol):
    eps = float(get_earnings_per_share(symbol))
    return eps

def calculate_pe_ratio(symbol):
    price = get_current_quote(symbol)
    eps = get_current_eps(symbol)
    print "eps got back is ",eps
    pe = price/eps
    return pe



#now = get_time()
#yesterday = get_time_yesterday(now)

#now_string = str(now)
#get_quote_download_dates()

#for instance in session.query(Stock).filter("date_added>'%s'" % yesterday):
    #print instance.call_sign

#print "today",now
#print "yesterday...hoefully:",yesterday


print_portfolio()

#get the current growth rate for a company. The online version keys directly into the yahoo API instead of local data. Of course this will change, but I figured I would lay the blue prints
#lets calculate the growth rate of some of the stocks I own

print "Calculating Growth Rates...:"
#calculate_growth_rate_online('ENB')
#calculate_growth_rate_online('MWE')
#calculate_growth_rate_online('SCCO')
calculate_growth_rate_online('WAG')
calculate_growth_rate_online('RAD')

pewag = calculate_pe_ratio('WAG')
print "Walgreens PE Ratio is ",pewag

perad = calculate_pe_ratio('RAD')
print "Rite Aid PE Ratio is ", perad
#get_quote_download_dates()
#get_current_quote('KMP')





