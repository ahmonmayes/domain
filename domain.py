#! python3
#Created 05/04/2021
#This program reads in a .txt file called 'domain.txt'
#Checks the MX records of the domain in the list and if it is regisered
#Outputs to the domCheck.csv

import sys
import whois
import dns.resolver
import csv

def lookup_mx(domain_name):
    try:
        text = []
        mailservers = dns.resolver.query(domain_name, 'MX')
        for data in mailservers:
            text.append(data.exchange)
    except Exception:
        return "Error"
    else:
        return text

def is_active(domain_name):
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)

with open('domain.txt') as fin:
    for line in fin:
        domain = line.strip()
        with open('domCheck.csv', 'a+', newline= '') as file:
            writer = csv.writer(file)
            writer.writerow([domain, is_active(domain),lookup_mx(domain)])
    






    

