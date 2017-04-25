from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import time
name=input("Enter a Pornstar name").split(" ")
error=0
page=1
counter=1
while(1):
    try:
        if len(name)>1:
            html=urlopen("https://www.pornhub.com/video/search?search=name[0]+name[1]&page="+str(page))
        else:
            html=urlopen("https://www.pornhub.com/video/search?search=name[0]&page="+str(page))
    except HTTPError as e:
        error=1
    if error==1:
        print("end")
        break
    else:
        soup=BeautifulSoup(html,"html.parser")
        soup=soup.find("ul",{"class":"videos search-video-thumbs"})
        l= soup.findAll("li",{"class":"videoblock videoBox"})
        for data in l:
            name=data.a.attrs['title']
            du=data.find("var",{"class":"duration"})
            duration=du.text
            print(str(counter)+" "+name+"   "+duration)
            print(" ")
            counter=counter+1
    page=page+1
    time.sleep(5)
    
            
            
            
        

