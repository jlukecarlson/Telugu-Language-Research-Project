import urllib2
from bs4 import BeautifulSoup
import sys
import string
import codecs
import traceback

alphabet = string.ascii_lowercase #'abcdefghijklmnopqrstuvwxyz'
# we already have a,b,c so start at d
alphabet = alphabet[3:]
browse_page = "http://www.shabdkosh.com/te/browse/"
base_url = "http://www.shabdkosh.com"
for letter in alphabet:
    sys.stderr.write(letter + "\n")
    try :
        req = urllib2.Request(browse_page + letter, headers={ 'User-Agent': 'Mozilla/5.0' })
        web_page = urllib2.urlopen(req).read()
        soup = BeautifulSoup(web_page)
        engl_words = soup.find_all(target='_blank')
        f = codecs.open(letter + "_telugu.csv", "w", "utf-8")
        for e in engl_words:
            e_text =  e.get_text()
            e_url = e['href']
            try:
                url = base_url + e_url.replace(" ", "%20")
                req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
                e_web_page = urllib2.urlopen(req).read()
                e_soup = BeautifulSoup(e_web_page)
                first_trans = e_soup.find("a", class_="in").get_text()
                f.write("%s,%s\n" % (e_text, first_trans))
                sys.stderr.write("%s,%s\n" % (e_text, first_trans))
            except:
                sys.stderr.write("Error for word %s and url %s !\n" % (e_text, url))
                traceback.print_exc(file=sys.stdout)
        f.close()
    #web_page = urllib2.urlopen("http://www.shabdkosh.com/te/translate/abundant/abundant-meaning-in-Telugu-English").read()
    #soup = BeautifulSoup(web_page)
    #c = soup.find("a", class_="in").get_text()
    except urllib2.HTTPError :
        sys.stderr.write("HTTPERROR!\n")
    except urllib2.URLError :
        sys.stderr.write("URLERROR!\n")
