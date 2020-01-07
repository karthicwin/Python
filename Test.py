import requests

import time

from bs4 import BeautifulSoup

# Set the URL you want to webscrape from

url = 'http://web.mta.info/developers/turnstile.html'

# Connect to the URL

response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶

soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags

for i in range(1,len(soup.findAll('a'))+1): #'a' tags are for links

    one_a_tag = soup.findAll('a')[i]
    
    link = one_a_tag['href']
    
    response1 = requests.get(link)
    
    soup1 = BeautifulSoup(response.text, "html.parser")
    
    for i in range(1,len(soup1.findAll('a'))+1): #'a' tags are for links

        one_a_tag1 = soup1.findAll('a')[i]
    
        link1 = one_a_tag1['href']
        
        download_url1 = one_a_tag1['href']
    
        #link = one_a_tag['href']

        # download_url = 'http://web.mta.info/developers/'+ link
    
        x = requests.get(download_url1,'./'+link1[link1.find('/turnstile_')+1:]) 
    
        print(x.text)
    
    time.sleep(1) #pause the code for a sec
    
#https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460


