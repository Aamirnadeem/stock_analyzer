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
    filter_string += "%' limit 1"
    for instance in session.query(Stock).filter("call_sign = '%s'" % call_sign).filter("%s" % filter_string):

        print instance.price,instance.call_sign,instance.date_added
        
    
#now = get_time()
#yesterday = get_time_yesterday(now)

#now_string = str(now)


#for instance in session.query(Stock).filter("date_added>'%s'" % yesterday):
    #print instance.call_sign

#for instance in session.query(Stock.date_added).distinct():
 #   print instance.date_added

#print "today",now
#print "yesterday...hoefully:",yesterday




#Use this function to pull quotes from the database
get_current_quote('CAH')
get_current_quote('KMP')
get_current_quote('ENB')
get_current_quote('SCCO')
get_current_quote('MWE')
