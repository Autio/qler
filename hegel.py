import pytumblr
import os

# Login
consumer_key ="shDKzPZtO61cI325oWiN9APV677NQJ2J5LyU1EPChAOWueQ27V"
consumer_secret ="eFjZ2hN3io13zigC27TgdK25PvkRV1FdjT4SX9YDL8AIqESqCE"
oauth_key = 'Iq0mE1Eg5FRuCOR5jz62i3ukPDQ09S2ezILJb1CYxV0XL8krB3'
oauth_secret ='6S8UPVXEtN5tafmCOQ4811UloUDFR04WjTZ1cakEpIWcSfCwAP'

client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_key,
    oauth_secret
)

print(client.info())

# Parameters for mass posting
folder = "C:\\Users\\X1\\Pictures\\Tumbulah\\H\\"
blogname = 'inbedwithhegel'
tags = ["Hegel", "Theory", "meme", "absolute idealism", "dialectic"]

# read in all photo names from folder, up to 300
posting_files = os.listdir(folder)

# cycle through them all and post as queue
for f in posting_files:

    #Creates a photo post using a local filepath
    client.create_photo(blogname, state="queue", tags=tags, caption="https://inbedwithhegel.tumblr.com", data=folder + f)
