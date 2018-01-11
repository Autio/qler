import pytumblr
import os
import xlsxwriter
import openpyxl
from random import shuffle

# Login
consumer_key ="uXvEN0L80Qo3wQNdFn1W3a9AjFd9nbPfRPwmU4mtAoXsnjoInI"
consumer_secret ="Lhcg8BOlAObOKPcKydS0QDtIvs3Lx83Pmu2cXO3zV40a2rAXth"
oauth_key = 'lb9dLU3LDiOE23tKh7oudLFDierd930YpfOesNQaZDkLaQZsLd'
oauth_secret ='6DDtVfBiKGfPjzZp7woKEXCQLLZCcpBH1kKCEu3ZSf2jtnNDMP'

client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_key,
    oauth_secret
)

print(client.info())

# Parameters for mass posting
folder = "C:\\Users\\X1\\Pictures\\Tumbulah\\EAA\\20171220c\\"
blogname = 'eastafricanart'
tags = ["East African Art", "Contemporary Art", "Modern Art", "Africa","Painting", "Colour"]

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

# cycle through them all and post as queuer
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
                client.create_photo(blogname, state="queue", tags=tags, caption= description + "\n\nSource: " + source.replace('"', '') + "\n\nMore East African Art: https://eastafricanart.tumblr.com", data=folder + f)
        except:
            print 'Could not upload file " + str(counter)'
    counter += 1


