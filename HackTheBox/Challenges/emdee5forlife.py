import requests
from pwn import *
from cmd import Cmd
from bs4 import BeautifulSoup




#need url and cookies
url = 'http://165.22.122.134:32465' #change this
cookies ={'PHPSESSID':'sr9of3nifm64gklbitdch8np56'} #change this
#make request initial request

page = requests.get(url,cookies=cookies)



while 'HTB{' not in page.text:
    
    get_hash= BeautifulSoup(page.text,features="html.parser").h3.contents[0]
    hashed = md5sumhex(get_hash.encode())
    
    page = requests.post(url,data={'hash':hashed}, cookies=cookies)


print("Here is the flag: " + BeautifulSoup(page.text,features="html.parser").p.contents[0])
