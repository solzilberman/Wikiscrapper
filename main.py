import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from urllib.request import urlopen

def getFive(links):
    ret = []
    for link in links:    
        ur = link.get('href')
        if ur != "" and ur != None:
            if "wiki" in ur:
                ret.append("https://en.wikipedia.org" + ur)
                if len(ret) == 5:
                    return ret


url = 'https://en.wikipedia.org/wiki/Alan_Turing'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a');
arr = getFive(links)
dic = {}
dic[url] = arr
for i in range(len(arr)):
    url = arr[i]
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    if links:
        dic[url] = getFive(links)
for key in dic:
    print(key[24:] + '\n')
    for i in range(len(dic[key])):
        print("   " + dic[key][i][24:] + '\n')
