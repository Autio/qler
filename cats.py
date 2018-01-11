import pytumblr
import os
import xlsxwriter
import openpyxl
from random import shuffle
# Login cyberpunk
consumer_key ="Yecrzdo536YlbM6hQILKHtyGojaqMJ3aAXKFsRTL9NYuAvKyRF"
consumer_secret ="nTS4tsrzOLV2TRnR6ESjaERgZkLTHFE8T5914f2zOaf6pwMG15"
oauth_key = 'DCCzb37q9MhWpL0XkjtwZEvK3fAtD9YTkqwaRHkZT2cVC9gfKa'
oauth_secret ='bJ7jTRXQwemExP4Yq5RM8vM7vMs8CBPARLinR9bugPVyzHjr8a'

client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_key,
    oauth_secret
)

print(client.info())

# Parameters for mass posting
folder = "C:\\Users\\X1\\Pictures\\Tumbulah\\catblast\\20171210b\\"
blogname = 'catblast'
tags = ["cats", "cat", "animal", "fun", "cute", "happy", "cuddly", "fluffy", "fur"]

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
                    description = line[2].strip("'").strip(',').strip('"')
                except:
                    print 'no description for file ' + str(counter)
               # Creates a photo post using a local filepath
                print 'Uploading file ' + str(counter)
                client.create_photo(blogname, state="queue", tags=tags, caption= "Source: " + source.replace('"', '') + "\n\nMore cats! https://catblast.tumblr.com", data=folder + f)
        except:
            print 'Could not upload file " + str(counter)'
    counter += 1