import pandas as pd

english = pd.DataFrame.from_csv("data/english.csv")
iden = english.id
iden = list(iden)

f = open("data/friendships/iden.txt")
iden = f.readlines()
f.close()

follower = []
followed = []
empty = []

for thisID in iden:
	friends_ids, followers_ids = get_friends_followers_ids(twitter_api, user_id=int(thisID), followers_limit=0)
	if len(friends_ids) > 0:
		with open("data/friendships/" + str(thisID) + ".txt" ,'w') as file:
			for item in friends_ids:
				print>>file, item
		for thisFriend in friends_ids:
			if thisFriend in iden:
				follower.append(thisID)
				followed.append(thisFriend)
	else:
		empty.append(thisID)

with open("data/friendships/empty.txt" ,'w') as file:
	for item in empty:
		print>>file, item