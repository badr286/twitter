from requests import post, get

class Twitter:
	def __init__(self, auth):
		self.auth = auth

		url = 'https://api.twitter.com/1.1/guest/activate.json'
		self.headers = {'authorization':self.auth}
		token = post(url, headers=self.headers).json()['guest_token']

		self.headers['x-guest-token'] = token

	def get_tweet_url(self, tweet_id):
		url = 'https://twitter.com/i/api/graphql/PiyMcWLe_7_E5ua3ICEJPQ/TweetDetail?variables='
		url+='{"focalTweetId":"'+tweet_id+'","with_rux_injections":false,"includePromotedContent":true,"withCommunity":true,"withQuickPromoteEligibilityTweetFields":false,"withTweetQuoteCount":true,"withBirdwatchNotes":false,"withSuperFollowsUserFields":false,"withUserResults":true,"withBirdwatchPivots":false,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":false,"withVoice":true}'
		return url

	def get_tweet(self, tweet_id):
		tweet_url = self.get_tweet_url(tweet_id)
		return get(tweet_url, headers=self.headers).json()

	def get_vid_sources(self, tweet_id):
		tweet = self.get_tweet(tweet_id)
		sources = tweet['data']['threaded_conversation_with_injections']['instructions'][0]['entries'][0]['content']['itemContent']['tweet_results']['result']['legacy']['extended_entities']['media'][0]['video_info']['variants']
		return sources

auth = 'Bearer ..'
user = Twitter(auth)
print(user.get_vid_sources('<tweet_id>'))
