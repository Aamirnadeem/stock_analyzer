import MySQLdb,datetime,re,argparse
from symbol import *
from database_classes import *
from time import strftime
from datetime import date


class StockAnalyzer:
    portfolio = []
    today = date.today()


    def __init__(self):
        pass

    def get_time(self):
        self.now = datetime.datetime.now()
        return self.now

    def get_time_yesterday(self):
        self.yesterday = self.today - datetime.timedelta(days=1)
        return self.yesterday
   
    def get_current_quote(self,call_sign):
        for instance in session.query(Stock).filter("call_sign = '%s'" % call_sign).order_by(desc(Stock.date_added)):
            return instance.price

    def calculate_growth_rate_online(self,symbol):
        future_eps = float(get_estimate_eps_next_year(symbol))
        current_eps = float(get_earnings_per_share(symbol))    

        #Calculate the Growth Rate
        delta_eps = future_eps - current_eps
        delta_eps *= 100
        delta_eps /= current_eps
        delta_eps_string = str(delta_eps)

        return delta_eps_string

    def get_quote_download_dates(self):
        for instance in session.query(Stock.date_added).distinct():
            print instance.date_added

    def print_portfolio(self):
        print self.get_current_quote('SCCO')
        print self.get_current_quote('KMP')
        print self.get_current_quote('MWE')
        print self.get_current_quote('ENB')

    def get_current_eps(self,symbol):
        eps = float(get_earnings_per_share(symbol))
        return eps

    def calculate_pe_ratio(self,symbol):
        price = self.get_current_quote(symbol)
        eps = self.get_current_eps(symbol)
        
        pe = price/eps

        return pe

    def calculate_snp_1yr_growth_rate(self):
        last_year = self.today.replace( year=self.today.year - 1 )

        last_year_day = last_year.replace( day = last_year.day + 1)
    
        string_today = self.today.strftime("%Y%m%d")
        string_last = last_year.strftime("%Y%m%d")
        string_last_day = last_year_day.strftime("%Y%m%d")

        snp_last = get_historical_prices("^GSPC", string_last,string_last_day)

        last_price = snp_last[1][4]
        today_price = get_price("^GSPC")

        net_change = float(today_price) - float(last_price)

        growth_rate = net_change / float(last_price)

        return growth_rate
    



#useful functions of the StockAnalyzer... more to come :)
Analyzer = StockAnalyzer()


print Analyzer.get_time()

print Analyzer.get_time_yesterday()
print Analyzer.get_current_quote("SCCO")
print Analyzer.calculate_growth_rate_online("SCCO")

#this function just dumps out all the dates I have to do a quick visual inspection of the indicies
#print Analyzer.get_quote_download_dates()

Analyzer.print_portfolio()

print Analyzer.get_current_eps("SCCO")
print Analyzer.calculate_pe_ratio("SCCO")
print Analyzer.calculate_snp_1yr_growth_rate()
