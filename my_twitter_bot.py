import tweepy
import time


CONSUMER_KEY = 'QsOhD9aP6UYDqWUhBCdYRGZPi'
CUNSUMER_SECRET = 'ngEpWLUzhvGrvrOTYGmcqI7e6B12XkfZg5UgtrGJh8MUBi0hbn'
ACCESS_KEY = '1489420375284924416-XHHHF2kj2QsHvQ1VoLs4YtOnH5c6rU'
ACCESS_SECRET = '4j8hRnAURg08BTqHa3o1rQIAyiYuWBbVhiqG3DUSlaqdo'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CUNSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def isPalindrome(tweet):
    s = ''.join(filter(str.isalnum, tweet))
    s = s.lower()
    slength = len(s)
    srev = ""
    while(slength != 0):
        srev = srev + s[slength-1]
        slength -= 1
    if s == srev:
        #if it is a palindrome
        palindrome = tweet + " is a palindrome"
        return palindrome
    else:
        #if it is not a palindrome
        palindrome = tweet + " is not a palindrome"
        return palindrome


FILE_NAME = "src/last_seen.txt"

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def run():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = "extended")



#to get tweets with a specific hashtag
    for tweet in reversed(tweets):
        if '#check' in tweet.full_text.lower():
            tweetText = tweet.full_text
            tweetText = tweetText.split()
            tweetText = tweetText[1:len(tweetText)-1]
            tweetText = str(tweetText)
            print(tweetText)
            isPalindrome(tweetText)
            # print(str(tweet.id) + " - " + tweet.full_text)
            api.update_status('@' + tweet.user.screen_name + " " + isPalindrome(tweetText).replace("[","").replace("]","").replace(",","").replace("\'",""), tweet.id)
            store_last_seen(FILE_NAME, tweet.id)


while True:
    run()
    time.sleep(20)

