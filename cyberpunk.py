import pytumblr
import os
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
folder = "C:\\Users\\X1\\Pictures\\Tumbulah\\cyberpunk\\20171121b\\"
blogname = 'cyberpunkonlypunk'
tags = ["cyberpunk", "dystopia", "future", "art", "cyber", "aesthetic", "mood", "vaporwave", "tech", "cyberspace", "chrome"]

# read in all photo names from folder, up to 300
posting_files = os.listdir(folder)

# cycle through them all and post as queue
for f in posting_files:
    shuffle(tags)
    #Creates a photo post using a local filepath
    client.create_photo(blogname, state="queue", tags=tags, caption="https://cyberpunkonlypunk.tumblr.com", data=folder + f)
