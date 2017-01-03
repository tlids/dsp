#output is seperated into single characters for each row?

import os
os.getcwd()

import csv

with open('emails.csv', 'w') as ef:
    a = csv.writer(ef, delimiter=',')
    email = faculty[' email']
    a.writerows(email)
    
ef.close

