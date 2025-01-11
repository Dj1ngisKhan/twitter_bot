from openai import OpenAI
import random
import tweepy

#TWITTER API (find your keys and insert them here):
api_key = ""
api_secret=""
bearer_token = r""
access_token = ""
access_token_secret = ""
twitter_client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

#GPT API:
client = OpenAI()



#GPT QUESTIONS:
tweets = ["Make a tweet about some a interesting theory about the universe that is less then 280 characters, 
"only include the content.",
"Make a tweet about a interesting theory about finance in the future, like 100 years from today"]
          
r_message = random.choice(tweets)



#ASKING GPT:
completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "system", "content": r_message}
  ]
)


tweet = completion.choices[0].message.content

tweet_test = ""

#SETTING UP TWITTER BOT:
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#SENDING TWEET:
twitter_client.create_tweet(text=tweet)
