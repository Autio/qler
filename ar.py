import pytumblr
import os

# Login vintagesailboats
consumer_key ="uXvEN0L80Qo3wQNdFn1W3a9AjFd9nbPfRPwmU4mtAoXsnjoInI"
consumer_secret ="Lhcg8BOlAObOKPcKydS0QDtIvs3Lx83Pmu2cXO3zV40a2rAXth"
oauth_key = 'xjhYmtwj4SWgj3Rb1XEjWQT7Q11plpYwsT7WOfp7GNhcPFpWIT'
oauth_secret ='ZJnTGrl1ZO5HgLWZ5Y4SNkYZv0rj41MLN4QtlHair6dB96RJNG'

client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_key,
    oauth_secret
)

print(client.info())

# Parameters for mass posting
folder = "C:\\Users\\X1\\Pictures\\Tumbulah\\AR\\20171018\\"
blogname = 'allthingsar'
tags = ["augmented reality", "ar", "vr", "mixed reality", "tech", "future", "new", "magic"]

# read in all photo names from folder, up to 300
posting_files = os.listdir(folder)

# cycle through them all and post as queue
for f in posting_files:

    #Creates a photo post using a local filepath
    client.create_photo(blogname, state="queue", tags=tags, caption="https://allthingsar.tumblr.com", data=folder + f)
