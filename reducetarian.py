import pytumblr
import os
from random import shuffle

# Login
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
folder = "C:\\Users\\X1\\Pictures\\Tumbulah\\Reducetarian\\"
blogname = 'reducetarianism'
tags = ["Reducetarian", "Flexitarian", "Healthy", "Easy", "Good", "Diet", "Food", "Nature", "Environment", "Vegan", "Vegetarian", "Consumption", "Meat"]

# read in all photo names from folder, up to 300
posting_files = os.listdir(folder)

# cycle through them all and post as queue
for f in posting_files:
    shuffle(tags)
    #Creates a photo post using a local filepath
    client.create_photo(blogname, state="queue", tags=tags, caption="https://reducetarianism.tumblr.com", data=folder + f)
