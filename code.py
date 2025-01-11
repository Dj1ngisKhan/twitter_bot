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
tweets = ["Make a tweet about some a interesting theory about the universe that is less then 280 characters, "
          "only include the content.",
          "Make a tweet about a interesting theory about finance in the future, like 100 years from today, "
          "only include the content, have it less the 280 characters long",
          "Make a tweet about a interesting conspiracy that I should post on twitter, make it less then 280 characters, "
          "also ask other users what their believes on this is? ChatGPT",
          "Make a short story less then 280 characters long, have a surprising plot twist at the end",
          "Make a short horror story less then 280 characters long, have a surprising plot tiwst at the end",
          "Make a short story about the universe less then 280 characters long, have a surprising plot tiwst at the end",
          "Make a dad joke as a tweet",
          "Relatable Experiences: Share humorous takes on common experiences. (Just tried to use my car keys to unlock "
          "my house. If anyone needs me, I'll be in bed reassessing my life choices.)",
          "Pet Antics: Pets are a goldmine for humor. My cat just stared at me for 10 minutes then knocked a "
          "glass off the table. Her message was clear: 'I own you.'",
          "Imaginary Scenarios: Create absurd hypothetical situations. Imagine if at the end of a marathon, they "
          "handed out free pizzas instead of medals. I bet record times would shatter."
          ]
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