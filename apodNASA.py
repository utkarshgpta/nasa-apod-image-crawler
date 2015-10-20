#/usr/bin/python

import requests
import urllib.request
import os
from bs4 import BeautifulSoup

def spider():
    directory = input("Enter the full path of the directory where you want to save the pictures: ")
    try:
        os.chdir(directory)
    except:
        print("ERR!: Unable to use the directory provided")
        os._exit(1)
    index_url = r'http://apod.nasa.gov/apod/archivepix.html'
    url = 'http://apod.nasa.gov/apod'
    source_code = requests.get(index_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    for link in soup.findAll('a'):
        href = link.get('href')
        if href[0] is 'a':
            imageDownload( url+'/'+href , url )

def imageDownload(url1 , url2):
    source_code = requests.get(url1)        
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")        # Crawls Each page in index, obtains image URL and downloads the image
    for link in soup.findAll('img'):
        src = link.get('src')
        url2 = url2 + '/' + src
        name = src[11:]
        print(name)
        urllib.request.urlretrieve(url2,name);

spider()
