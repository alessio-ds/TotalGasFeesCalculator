# -*- coding: utf-8 -*-
"""
Created on Mon May  3 18:43:36 2021

@author: alessiosca
"""

import requests


print("\nTotal Gas Fees Calculator (for BinanceSmartChain)\n")


address=input('Input your address: ')
apikey=input('Input your APIkey (get it from https://bscscan.com/myapikey): ')
bscscan="https://api.bscscan.com/api?module=account&action=txlist&address="+address+"&startblock=1&endblock=99999999&sort=asc&apikey="+apikey
#0x35C94C8f76ddFF652c259e67F822a508e857F1Cf


page=requests.get(bscscan)
pagetext=page.text


s='"nonce":"'
d=100
c='"'
for _ in range(100):
    fuck=(s+str(d)+c)
    ntx=pagetext.find(fuck)
    if ntx==-1:
        d-=1
    else:
        break

gastot=0
for nonce in range(d):

    pos=pagetext.find('"gasUsed":"')
    gas=(pagetext[pos+11:pos+18])
    try:
        gas=float(gas)
    except:
        gas=(pagetext[pos+11:pos+17])
        try:
            gas=float(gas)
        except:
            gas=(pagetext[pos+11:pos+16])
            gas=float(gas)
    gastot+=gas        
    pagetext=pagetext.replace(pagetext[:pos+100], '')

    

epic="https://nomics.com/assets/gwei-gwei"
page=requests.get(epic)
pagetext=page.text
poscost=pagetext.find("$0.00000")
gascost=pagetext[poscost+1:poscost+11]
try:
    gascost=float(gascost)
except:
    gascost=pagetext[poscost+1:poscost+10]
    try:
        gascost=float(gascost)
    except:
        gascost=pagetext[poscost+1:poscost+9]
        gascost=float(gascost)
        
gasusd=gastot*gascost

print("Total Transactions:", d)
print("Actual gwei cost in USD: $",format(gascost,'.12f'))
print("Total gas spent:", gastot, "( $",format(gasusd,'.2f'),")")

input('')

