# saved code for using x api to fetch tweets

API_KEY = "5iACuCVrhkZkGlqoLG51sTguQ"

API_KEY_secret = "th17t3yUOTsRjsTLA6PxHbvs1iHURw0kKINTnQNatYtM2fqwPw"

# Authenticate to the API
bearer_token = "AAAAAAAAAAAAAAAAAAAAAPfHrgEAAAAASmQ5Yr3VQGUC2dDoOsEqxpBiJJo%3DMeYCyY0yQfZMrKE5a1Vh280irG0Mwyj5CUlhQ1Tbhx9ZcV82do"
client = tweepy.Client(bearer_token=bearer_token)

# Define the search query
query = "Tesla -is:retweet"

try:
    # Get the tweets using API v2
    tweets = client.search_recent_tweets(
        query=query, tweet_fields=["text"], max_results=100
    )

    # Check if tweets were returned
    if tweets.data:
        # Create a list to store the tweets
        tweets_list = [[tweet.text] for tweet in tweets.data]

        # Create a DataFrame from the list
        tweets_df = pd.DataFrame(tweets_list, columns=["text"])

        # Display the first few rows of the DataFrame
        print(tweets_df.head())
    else:
        print("No tweets found for the given query.")

except tweepy.TweepyException as e:
    print(f"An error occurred: {e}")
