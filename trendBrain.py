import shlex

tweets = ""
tweetCount = input("Enter Tweets with starting as tweets count: ")
for tweet in range(int(tweetCount)):
	tweets+=input()+"\n"

tweetWords = shlex.split(tweets)
hashTags = [tweetWord for tweetWord in tweetWords if tweetWord.startswith('#')]
hashTagWithCounts = dict((hashTag,hashTags.count(hashTag)) for hashTag in set(hashTags))
highestCountHashTags = sorted(hashTagWithCounts.items(), key=lambda hashTag: (-hashTag[1], hashTag[0]))
top5HashTags = highestCountHashTags[:5]

print("Top 5 trending Tweets:")
for hashTag, count in top5HashTags:
	print(hashTag)
