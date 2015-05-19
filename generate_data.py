#!/usr/bin/env python

"""Generate random data."""

#---Import necessary libraries---#
import sys
import os
import numpy as np
import string
import random as rand
from datetime import datetime
import names
import unicodedata

#---Functions---#
def rand_string(size=5, chars=string.ascii_lowercase + string.digits):
        return ''.join(rand.choice(chars) for _ in range(size))
def rand_date(yr_down, yr_up, month_down, month_up, day_down, day_up):
        year = rand.randint(yr_down, yr_up)
        month = rand.randint(month_down, month_up)
        day = rand.randint(day_down, day_up)
        new_date = str(datetime(year, month, day))
        return new_date

#---Processing---#
domain = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@aol.com']
data_len = 50
new_file = open('random_data.txt', 'w')
print >> new_file, 'name lastname email domain date'
for i in xrange(data_len):
        uname = names.get_full_name()
        full_name = unicodedata.normalize('NFKD', uname).encode('ascii','ignore')
        username = rand_string()
        rand_domain = rand.choice(domain)
        email = username+rand_domain
        get_date = rand_date(2013, 2015, 1, 12, 1, 28)
        new_file.write(full_name+' '+email+' '+rand_domain+' '+get_date+'\n')
new_file.close()

