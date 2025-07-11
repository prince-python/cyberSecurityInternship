import theHarvester
from theHarvester.discovery import bingsearch
from theHarvester.discovery import googlesearch

#....and more....
# or
# from theHarvester.discovery import *

baidu = baidusearch.SearchBaidu("google", 100)
baidu.do_search()

# Each discovery engine has it's own method
# not all have get_emails

emails = baidu.get_emails()
hostnames = baidu.get_hostnames()
print("Emails found:", emails)
print("Hostnames found:", hostnames)