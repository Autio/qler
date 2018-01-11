import pytumblr
import os

# Login
consumer_key ="Fu5JrC1Dl6ziquswT4afodDeoScthdUEdlzver8iHi0xK68wbR"
consumer_secret ="hCML7Ym4ESNiSYpvyosiO5PYF2COPRXBiD7vIlnkabBtxxunkQ"
oauth_key =  'om1EokxT98eddxHzvglSpIzPVqcAizGWy1Qn2qdvH1ZQi3jvkS'
oauth_secret ='ycLsERQ8NDGLDkn8AqyNvscF6metNtdWWMdlrjpCDkCK1HFey4'

client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_key,
    oauth_secret
)

print(client.info())

# Parameters for mass posting
folder = "C:\\Users\\X1\\Pictures\\Tumbulah\\digitalnomad\\3\\"
blogname = 'digitallynomad'
tags = ["digital", "nomad", "freedom", "travel", "lifestyle", "laptop", "remote work", "vagabond", "modern life", "travelling", "abroad", "work", "adventure", "dream", "lust for adventure"]

# read in all photo names from folder, up to 300
posting_files = os.listdir(folder)

# cycle through them all and post as queue
for f in posting_files:

    #Creates a photo post using a local filepath
    client.create_photo(blogname, state="queue", tags=tags, caption="https://digitallynomad.tumblr.com", data=folder + f)
