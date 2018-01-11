import pytumblr
import os
import xlsxwriter
import openpyxl
from random import shuffle
# Login cyberpunk
consumer_key ="uXvEN0L80Qo3wQNdFn1W3a9AjFd9nbPfRPwmU4mtAoXsnjoInI"
consumer_secret ="Lhcg8BOlAObOKPcKydS0QDtIvs3Lx83Pmu2cXO3zV40a2rAXth"
oauth_key = 'WyDrctpcXo0C9yedXlhfaSMINNubPDsaULPvAziwClJsMBKdDC'
oauth_secret ='2SNQXPFU4pRtSnHFSMciyzgr3Bzi9HVKpPELssITiq9FnxeBBQ'

client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_key,
    oauth_secret
)

print(client.info())

# Parameters for mass posting
folder = "C:\\Users\\X1\\Pictures\\Tumbulah\\cyberpunk\\20171217\\"
blogname = 'cyberpunkonlypunk'
tags = ["cyberpunk", "dystopia", "future", "art", "cyber", "aesthetic", "mood", "vaporwave", "tech", "cyberspace", "chrome", "cybernetic"]

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
                client.create_photo(blogname, state="queue", tags=tags, caption= description + "\n\n<a href = \"" + source.replace('"', '') + "\">Source</a>\n\nMore cyberpunk: https://cyberpunkonlypunk.tumblr.com", data=folder + f)
        except:
            print 'Could not upload file " + str(counter)'
    counter += 1