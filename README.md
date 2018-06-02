# Twitter Trending HashTags

## Problem Description
Twitter shows trends in order to make its users aware of the trending news. These trends are nothing but trending hashtags that the users are tweeting about. For example: If thousands of users are talking about United States by adding a hashtag #US in their tweet, then US will be a trending hashtag. Couple of example tweets with hashtag #US could be:

Donald Trump becomes the 45th #US President
Roger Federer wins #US Open for 5th time
Given a list of N tweets, your task is to find top the five trending hashtags. Each tweet, let's call it S, will contain at least one one word with hashtag. There will be maximum of three hashtags in any tweet. All hashtags in a single tweet will be unique.

## Input
First line of the input will contain N denoting the number of tweets.
Next N lines, each will contain a string S.

## Output
Print the top five trending hashtags. In case of tie between any two hashtags, print them in lexicographical order in a new line.

## Constraints
10 ≤ N ≤ 10^3
1 ≤ | S | ≤ 140 where S denotes length of string S i.e. length of tweet.
Any hashtag denoted by H 1 ≤ | H | ≤ 20 where H denotes length of any hashtag H.

### Note
Any tweet is composed of lowercase and uppercase English letters, digits and spaces.
Any hashtag begins with # and the subsequent characters will only contain lowercase and uppercase English letters and digits.

## Sample Input
	10
	Donald Trump becomes the 45th #US President
	Potentially habitable exoplanet #ProximaB discovered
	#RogerFederer wins #US Open for 5th time
	#GravitationalWaves detection successful
	Traces of liquid water discovered on #Mars
	Life Could Survive on Exoplanet #ProximaB
	Go go #RogerFederer
	Ten ways #ProximaB is different from Earth
	ISRO becomes 4th space agency to reach #Mars
	#RogerFederer beats #Nadal

## Sample Output
	#ProximaB
	#RogerFederer
	#Mars
	#US
	#GravitationalWaves

## Usage
1. Clone project repo: `git@github.com:hari696/twitter_hash_tag.git`
2. Run `python trendBrain.py`
3. Give the same tweet as input
4. Now you can see the Top Five trending Tweets
