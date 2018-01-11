import pytumblr
import os
from random import shuffle

# Login vintagesailboats
consumer_key ="L21i6Chczdooz2RgQlQ5F6y4BlbJ5e0a9E1NPQSPwRjuF90lIk"
consumer_secret ="PdcLhbgXBNuBSMnJEVovi3IoQIfTmGMArMpFC23rdVPaJKg9IW"
oauth_key ="cPjhg9OcCmU6FHwgaxuxxJczv6grgxpWjqGefh4rVT145cFMpT"
oauth_secret ="dlRzsieXkkzaWy4y9K96JOSeKwJPEjcIcnLuJrhZ3WubDruOmc"

client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_key,
    oauth_secret
)

print(client.info())

# Parameters for mass posting
folder = "C:\\Users\\X1\\Pictures\\Tumbulah\Sail\\20171121\\"
blogname = 'vintagesailboats'
tags = ["sea", "vintage", "classic", "sailing", "seafaring", "boat", "ship", "vintage sail boat", "yacht", "lifestyle", "timeless", "adventure", "spirit", "ocean", "freedom", "life"]

# read in all photo names from folder, up to 300
posting_files = os.listdir(folder)

# cycle through them all and post as queue
for f in posting_files:
    shuffle(tags)
    #Creates a photo post using a local filepath
    client.create_photo(blogname, state="queue", tags=tags, tweet="Vintage sailboats", caption="https://vintagesailboats.tumblr.com", data=folder + f)
