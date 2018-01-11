import pytumblr
import os
import csv
from datetime import datetime

logins = []
stats = [] # name, followers, posts, queue

# login east african art
consumer_key ="uXvEN0L80Qo3wQNdFn1W3a9AjFd9nbPfRPwmU4mtAoXsnjoInI"
consumer_secret ="Lhcg8BOlAObOKPcKydS0QDtIvs3Lx83Pmu2cXO3zV40a2rAXth"
oauth_key = 'lb9dLU3LDiOE23tKh7oudLFDierd930YpfOesNQaZDkLaQZsLd'
oauth_secret ='6DDtVfBiKGfPjzZp7woKEXCQLLZCcpBH1kKCEu3ZSf2jtnNDMP'
logins.append([consumer_key, consumer_secret, oauth_key, oauth_secret])

# Login ar
consumer_key ="uXvEN0L80Qo3wQNdFn1W3a9AjFd9nbPfRPwmU4mtAoXsnjoInI"
consumer_secret ="Lhcg8BOlAObOKPcKydS0QDtIvs3Lx83Pmu2cXO3zV40a2rAXth"
oauth_key = 'xjhYmtwj4SWgj3Rb1XEjWQT7Q11plpYwsT7WOfp7GNhcPFpWIT'
oauth_secret ='ZJnTGrl1ZO5HgLWZ5Y4SNkYZv0rj41MLN4QtlHair6dB96RJNG'
logins.append([consumer_key, consumer_secret, oauth_key, oauth_secret])

# Login cyberpunk
consumer_key ="uXvEN0L80Qo3wQNdFn1W3a9AjFd9nbPfRPwmU4mtAoXsnjoInI"
consumer_secret ="Lhcg8BOlAObOKPcKydS0QDtIvs3Lx83Pmu2cXO3zV40a2rAXth"
oauth_key = 'WyDrctpcXo0C9yedXlhfaSMINNubPDsaULPvAziwClJsMBKdDC'
oauth_secret ='2SNQXPFU4pRtSnHFSMciyzgr3Bzi9HVKpPELssITiq9FnxeBBQ'
logins.append([consumer_key, consumer_secret, oauth_key, oauth_secret])

# Login reducetarianism
consumer_key ="3XGG0iug2h2u8PnzpVynpbfQFCvi90xW5Nj4cebB4VRgPm0glx"
consumer_secret ="8qwtdpum87mB9SxRV0RmPrG2ONUwJbbxa3q6w6bKHdElW6ArnI"
oauth_key = 'Lb6mdMHxOQpHL8gebPmvqgRKexjTD1XmfqA0l1483WwbC6vyV5'
oauth_secret ='QPSDmYxgx67Gv6QUq5zRRMjv6PeQpkKsPtFynxKsAYIh4pMJUY'
logins.append([consumer_key, consumer_secret, oauth_key, oauth_secret])

# Login vintagesailboats
consumer_key ="L21i6Chczdooz2RgQlQ5F6y4BlbJ5e0a9E1NPQSPwRjuF90lIk"
consumer_secret ="PdcLhbgXBNuBSMnJEVovi3IoQIfTmGMArMpFC23rdVPaJKg9IW"
oauth_key ="cPjhg9OcCmU6FHwgaxuxxJczv6grgxpWjqGefh4rVT145cFMpT"
oauth_secret ="dlRzsieXkkzaWy4y9K96JOSeKwJPEjcIcnLuJrhZ3WubDruOmc"
logins.append([consumer_key, consumer_secret, oauth_key, oauth_secret])

# Login digital nomad
consumer_key ="Fu5JrC1Dl6ziquswT4afodDeoScthdUEdlzver8iHi0xK68wbR"
consumer_secret ="hCML7Ym4ESNiSYpvyosiO5PYF2COPRXBiD7vIlnkabBtxxunkQ"
oauth_key =  'om1EokxT98eddxHzvglSpIzPVqcAizGWy1Qn2qdvH1ZQi3jvkS'
oauth_secret ='ycLsERQ8NDGLDkn8AqyNvscF6metNtdWWMdlrjpCDkCK1HFey4'
logins.append([consumer_key, consumer_secret, oauth_key, oauth_secret])

# Login warhammer
consumer_key ="uXvEN0L80Qo3wQNdFn1W3a9AjFd9nbPfRPwmU4mtAoXsnjoInI"
consumer_secret ="Lhcg8BOlAObOKPcKydS0QDtIvs3Lx83Pmu2cXO3zV40a2rAXth"
oauth_key =  'G4BX1U6kTakysSvmpFeLLJ23MgLl5d2gjHuNMnCxCf4dK2oO3s'
oauth_secret ='n4OuwGmo2FVSnlJNQbE1E1SUIt0xtma846DWhdDykQGHaF46ot'
logins.append([consumer_key, consumer_secret, oauth_key, oauth_secret])


# login hegel
consumer_key ="shDKzPZtO61cI325oWiN9APV677NQJ2J5LyU1EPChAOWueQ27V"
consumer_secret ="eFjZ2hN3io13zigC27TgdK25PvkRV1FdjT4SX9YDL8AIqESqCE"
oauth_key = 'Iq0mE1Eg5FRuCOR5jz62i3ukPDQ09S2ezILJb1CYxV0XL8krB3'
oauth_secret ='6S8UPVXEtN5tafmCOQ4811UloUDFR04WjTZ1cakEpIWcSfCwAP'
logins.append([consumer_key, consumer_secret, oauth_key, oauth_secret])

totalFollowers = 0

for l in logins:
    try:
        client = pytumblr.TumblrRestClient(
            l[0],
            l[1],
            l[2],
            l[3]
        )
        info = client.info()
        followers = info['user']['blogs'][0]['followers']
        name = info['user']['blogs'][0]['name']
        posts = info['user']['blogs'][0]['posts']
        queue = info['user']['blogs'][0]['queue']

        stats.append([name, followers, posts, queue])
        totalFollowers += followers
    except:
        print("could not login")


# Go through all the accounts and keep track of key stats


print(stats)

# save these down into the main CSV with a timestamp
with open('timesheet.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    for r in stats:
        r.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        writer.writerow(r)

print(totalFollowers)