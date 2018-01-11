import pytumblr
import os

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
folder = "C:\\Users\\X1\\Pictures\\Tumbulah\\EAA\\20171115\\"
blogname = 'eastafricanart'
tags = ["East African Art", "Contemporary Art", "Modern Art", "Africa", "Uganda"]

# read in all photo names from folder, up to 300
posting_files = os.listdir(folder)

# cycle through them all and post as queue
for f in posting_files:

    #Creates a photo post using a local filepath
    client.create_photo(blogname, state="queue", tags=tags, caption="https://eastafricanart.tumblr.com", data=folder + f)
