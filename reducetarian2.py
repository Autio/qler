import pytumblr
import os
import xlsxwriter
import openpyxl
from random import shuffle
# Login cyberpunk
consumer_key ="3XGG0iug2h2u8PnzpVynpbfQFCvi90xW5Nj4cebB4VRgPm0glx"
consumer_secret ="8qwtdpum87mB9SxRV0RmPrG2ONUwJbbxa3q6w6bKHdElW6ArnI"
oauth_key =  'Lb6mdMHxOQpHL8gebPmvqgRKexjTD1XmfqA0l1483WwbC6vyV5'
oauth_secret ='QPSDmYxgx67Gv6QUq5zRRMjv6PeQpkKsPtFynxKsAYIh4pMJUY'

client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_key,
    oauth_secret
)

print(client.info())

# Parameters for mass posting
folder = "C:\\Users\\X1\\Pictures\\Tumbulah\\reducetarian\\20171220e\\"
blogname = 'reducetarianism'
tags = ["Reducetarian", "Flexitarian", "Healthy", "Easy", "Good", "Diet", "Food", "Nature", "Environment", "Vegan", "Vegetarian", "Consumption", "Meat Free", "Life", "Lifestyle", "Ethical", "Moral", "Good life"]

# read in all photo names from folder, up to 300
posting_files = os.listdir(folder)

index = []
# Read index file
wb = openpyxl.load_workbook(folder + "index.xlsx")
ws = wb['Sheet1']

for row in ws.rows:
    line = []
    for cell in row:
        line.append(cell.value)
    index.append(line)
#with open(folder + 'index.csv', 'r') as myfile:
#    for line in myfile:
#        index.append(line.strip().split('|'))

# Only output files which have a corresponding line in the index file

bitcoinref = "<a href='https://bit.do/free_bitcoins'>Bonus: Free Bitcoins every hour</a>"

# cycle through them all and post as queue
counter = 1
for f in posting_files:
    shuffle(tags)
    for line in index:
        try:
            if(line[0].strip('"') == f):
                source = line[1]
                description = ""
                try:
                    description = line[2].strip("'").strip(',')
                except:
                    print 'no description for file ' + str(counter)
               # Creates a photo post using a local filepath
                print 'Uploading file ' + str(counter)
                client.create_photo(blogname, state="queue", tags=tags, caption=  description + "\n\n<a href = \"" + source.replace('"', '') + "\">Source</a>\n\nMore healthy eating: https://reducetarianism.tumblr.com" + "<br><br>" + bitcoinref , data=folder + f)
        except:
            print 'Could not upload file " + str(counter)'
    counter += 1