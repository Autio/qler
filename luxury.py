import pytumblr
import os

# Login cyberpunk
consumer_key ="FBjcksK6m4JZR02EoQElB6BULs3refDddcsIvT3OLKlYywB6zy"
consumer_secret ="vnIHzPIlQjNZ75T5X0qzAJQYViO9UfOghJyPPR8vwvcaOsntlv"
oauth_key = 'DZQmpxRh9yJPmmiMk8kWPvargoclHVRqzY0b3HygsCU1rt5hP9'
oauth_secret ='UOvhBCfLxWJQ8L0S5UKiuPgim6YrEsSkM0OQglysJM3cOE0v0G'

client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_key,
    oauth_secret
)

print(client.info())

# Parameters for mass posting
folder = "C:\\Users\\X1\\Pictures\\Tumbulah\\Deluxe\\20171122\\"
blogname = 'lifedeluxe'
tags = ["luxury", "lavish", "lifestyle", "deluxe", "lush", "wealth", "drive", "desire", "class", "success", "dream", "beauty"]

# read in all photo names from folder, up to 300
posting_files = os.listdir(folder)

# cycle through them all and post as queue
for f in posting_files:

    #Creates a photo post using a local filepath
    client.create_photo(blogname, state="queue", tags=tags, caption="https://lifedeluxe.tumblr.com", data=folder + f)
