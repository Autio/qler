import pytumblr
import os
import csv
from datetime import datetime
import openpyxl
import sys
reload(sys)
sys.setdefaultencoding('utf8')


logins = []
stats = [] # name, followers, posts, queue

# Read in stats from the control file
class TumblrBlog(object):
    def __init__(self, id, name, password, consumerKey, consumerSecret, oauthKey, oauthSecret, tags, keywords):
        self.id = id
        self.name = name
        self.password = password
        self.consumerKey = consumerKey
        self.consumerSecret = consumerSecret
        self.oauthKey = oauthKey
        self.oauthSecret = oauthSecret
        self.tags = tags
        self.keywords = keywords

mainFile = openpyxl.load_workbook("control file.xlsx")
mainSheet = mainFile['Sheet1']
headerRow = True
tumblrData=[]

for row in mainSheet.rows:
    if not headerRow:
        line = []
        for cell in row:
            line.append(cell.value)
        tumblrData.append(
            TumblrBlog(line[0], line[1], line[4], line[5], line[6], line[7], line[8], line[9].split(','), line[10]))
    else:
        headerRow = False

for tumblr in tumblrData:
    consumer_key = str(tumblr.consumerKey)
    consumer_secret = str(tumblr.consumerSecret)
    oauth_key = str(tumblr.oauthKey)
    oauth_secret = str(tumblr.oauthSecret)
    logins.append([consumer_key, consumer_secret, oauth_key, oauth_secret])

totalFollowers = 0
totalNotes = 0
for l in logins:
    try:
        client = ""

        info = pytumblr.TumblrRestClient(
            str(l[0]),
            str(l[1]),
            str(l[2]),
            str(l[3])
        ).info()
        followers = info['user']['blogs'][0]['followers']
        name = info['user']['blogs'][0]['name']
        posts = info['user']['blogs'][0]['posts']
        queue = info['user']['blogs'][0]['queue']
        stats.append([name, followers, posts, queue])
        totalFollowers += followers
    except Exception, e:
        print 'Failed to login: ' + str(e)

# Go through all the accounts and keep track of key stats
print(stats)

# save these down into the main CSV with a timestamp
with open('timesheet.csv', 'ab') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    for r in stats:
        r.append(datetime.now().strftime('%Y-%m-%d'))
        writer.writerow(r)

print(totalFollowers)