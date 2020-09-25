#imports
from datetime import datetime
import urllib.request
import os
from urllib.request import urlretrieve
import sys

#get copy to local file
urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "save.log")
x = open("save.log", "r")
URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
my_copy = 'save.log'
#open/read
x = open("save.log", "r")

#vars
total_number_request = 0
number_of_error = 0
number_of_redirect = 0
date = []
weeks = {}
months = {}
files = {}
days = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}

for line in x:
    lines = line.split(" ")
    if len(lines) < 10:
        continue
    total_number_request += 1

print("How many requests were made: ", total_number_request)

#didnt get to the other parts :*(
##How many requests were made on a week-by-week basis? Per month?
##What percentage of the requests were not successful (any 4xx status code)?
##What percentage of the requests were redirected elsewhere (any 3xx codes)?
##What was the most-requested file?
##What was the least-requested file?
