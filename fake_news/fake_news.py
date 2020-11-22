'''
@Author:Yohannes Assebe(John Assebe)
web scraper(from two sites)
'''

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
from urllib.request import Request 
from textblob import TextBlob
from subprocess import Popen
import threading
import io
f=io.open("fake_news.txt", "w", encoding="utf-8")
def am_mass_media():
        url_am_media='https://www.amharaweb.com/category/%e1%8b%9c%e1%8a%93/national/'
        req_am_media=Request(url_am_media, headers={'User-Agent': 'Mozilla/5.0'})
        am_media_client=ureq(req_am_media)
        html_page2=am_media_client.read()
        am_media_client.close()
        page_soup_am=soup(html_page2,'html.parser')
        am_containers=page_soup_am.findAll('div',{'class':'td-module-thumb'})
        # print(len(am_containers))
        for container in am_containers:
                
                if(len(container.img['title'])>15):
                        print("መረጃው የተጠናቀረው ከ https://www.amharaweb.com ነው",file=f)
                        print(container.img['title'],file=f)
                        print("=============================================================",file=f)
                        print('\n',file=f)
	
def from_horn_affair():
        for i in range(2):
                url_horn_affair='https://hornaffairs.com/am/category/tplf/page/'+str(i+1)
                req=Request(url_horn_affair, headers={'User-Agent': 'Mozilla/5.0'})
                horn_affair_client=ureq(req)
                html_page=horn_affair_client.read()
                horn_affair_client.close()
                page_soup=soup(html_page,'html.parser')
                containers=page_soup.findAll('div',{'class':'post-design-content'})
                for container in containers:
                        

                        container=container.findAll('div',{'class':'post-content-area'})[1]
                        container_links=container.findAll('a',href=True)
                        for i in container_links:
                                lan=TextBlob(i.text)
                                if len(i.text)>=10 and lan.detect_language()=='am':
                                        print("መረጃው የተጠናቀረው ከ https://hornaffairs.com ነው",file=f)
                                        print(i.text+'\n',file=f)
                                        print("=============================================================",file=f)
                                        print('\n',file=f)

if __name__ == '__main__':
        thread1=threading.Thread(target=am_mass_media)
        thread1.start()
        from_horn_affair()
        f.close()
        Popen(['start','fake_news.txt'],shell=True)
