from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import xlsxwriter
import cookielib
import json
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# read in a list of search terms

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

imageList = []
query = raw_input("Search terms") # you can change the query for the image  here
image_type="ActiOn"
query= query.split()
query='+'.join(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print url
#add the directory for your image here
DIR="C:\\Pictures\\"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)


ActualImages=[]# contains the link for Large original images, type of  image
for a in soup.find_all("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    desc = json.loads(a.text)["s"]
    desc = desc.replace('\\u', '')
    ActualImages.append([link,Type,desc])

print  "there are total" , len(ActualImages),"images"

if not os.path.exists(DIR):
            os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])

if not os.path.exists(DIR):
            os.mkdir(DIR)
###print images
for i , [img, Type, desc] in enumerate(ActualImages):
    try:
        req = urllib2.Request(img, headers={'User-Agent' : header})
        raw_img = urllib2.urlopen(req).read()

        cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        print cntr
        if len(Type)==0:
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
            imageList.append([image_type + "_" + str(cntr)+".jpg", img.encode('utf-8'), desc.encode('utf-8')])

        else :
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')
            imageList.append([image_type + "_"+ str(cntr)+"."+Type, img.encode('utf-8'), desc.encode('utf-8')])


        f.write(raw_img)
        f.close()
    except Exception as e:
        print "could not load : "+img
        print e

print imageList
workbook = xlsxwriter.Workbook(DIR + '\\index.xlsx')
worksheet = workbook.add_worksheet()
for row in range(len(imageList)):
    worksheet.write(row, 0, imageList[row][0])
    worksheet.write(row , 1, imageList[row][1])
    worksheet.write(row , 2, imageList[row][2])
workbook.close()

#with open(DIR + '\\index.csv', 'wb') as myfile:
#    wr = csv.writer(myfile, delimiter='|', quoting=csv.QUOTE_ALL)
#    wr.writerow(row)