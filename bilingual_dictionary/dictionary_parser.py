import urllib2
from bs4 import BeautifulSoup
import sys
import string
import codecs

alphabet = string.ascii_lowercase #'abcdefghijklmnopqrstuvwxyz'
browse_page = "http://www.shabdkosh.com/te/browse/"
base_url = "http://www.shabdkosh.com"
try :
    web_page = urllib2.urlopen(browse_page).read()
    soup = BeautifulSoup(web_page)
    engl_words = soup.find_all(target='_blank')
    f = codecs.open("a_telugu.csv", "w", "utf-8")
    i = 0
    for e in engl_words:
        i += 1
        if i == 10:
            break
        e_text =  e.get_text()
        e_url = e['href']
        try:
            url = base_url + e_url.replace(" ", "%20")
            e_web_page = urllib2.urlopen(url).read()
            e_soup = BeautifulSoup(e_web_page)
            first_trans = e_soup.find("a", class_="in").get_text()
            f.write("%s,%s\n" % (e_text, first_trans))
            sys.stderr.write("%s,%s\n" % (e_text, first_trans))
        except:
            sys.stderr.write("Error for word %s and url %s !\n" % (e_text, url))
    
    #web_page = urllib2.urlopen("http://www.shabdkosh.com/te/translate/abundant/abundant-meaning-in-Telugu-English").read()
    #soup = BeautifulSoup(web_page)
    #c = soup.find("a", class_="in").get_text()
except urllib2.HTTPError :
    sys.stderr.write("HTTPERROR!\n")
except urllib2.URLError :
    sys.stderr.write("URLERROR!\n")
