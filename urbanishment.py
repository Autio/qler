import pytumblr
import os
import xlsxwriter
import openpyxl
from random import shuffle
# Login cyberpunk
consumer_key ="Z8SbqHfA3jx4w3KJnubvJsNUEKRXgzXim9ojiEHUtaieahs2tz"
consumer_secret ="DnxWBowjhJntjy6zVjDdaSvnqdH1aRy17yyU2Timtk82k2kcpo"
oauth_key =  'ENpvjbtCS78COOeo0b34yEBllcfkMdusBXHXtzO7XvzrGw8ZWx'
oauth_secret ='cteNI1oG76zsX4VLlPvjXJoQfTlQsXMemjkkyPVbNF8ocZCYYy'

client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_key,
    oauth_secret
)

print(client.info())

# Parameters for mass posting
folder = "C:\\Users\\X1\\Pictures\\Tumbulah\\urbanishment\\20171221\\"
blogname = 'urbanishment'
tags = ["urban", "city", "cities", "cityscape", "buildings", "architecture", "construct", "build", "modern"]

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
                client.create_photo(blogname, state="queue", tags=tags, caption=  description + "\n\n<a href = \"" + source.replace('"', '') + "\">Source</a><br<br>>\n\nhttps://urbanishment.tumblr.com" + "<br><br>" + bitcoinref , data=folder + f)
        except:
            print 'Could not upload file " + str(counter)'
    counter += 1