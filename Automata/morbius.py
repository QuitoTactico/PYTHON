# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 23:11:13 2022
@author: Hoss
"""
#Imports... Duh
from nltk.stem import LancasterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from random import sample
import string
import math
import nltk
import tweepy
import time

#Needed Keys and secrets for accessing Twitter API
consumer_key='*Insert Consumer Key Here*'
consumer_secret='*Insert Consumer Secret Here*'
access_token='*Insert Access Token Here*'
access_token_secret='*Insert Access Token Secret Here*'
bearer_token='*Insert Bearer token here*'
#Twitter ID for the New York Times
nytimesid=807095


#Building the Tweepy Client to connect to twitter
client = tweepy.Client(bearer_token=bearer_token)
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

#Seperator used to remove links from the tweets
seperator="http"
#Fields needed from tweets pulled from API
tweet_fields=["text", "lang", "public_metrics"]
#Parts of the senteces we want to change. All forms of Nouns and verbs. 
#This could be updated to work on adjectives, etc. but i never got it to look right after being changed
#List of types https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
goodParts=['NN','NNS','NNP','NNPS','RB','RBR','RBS','VB','VBG','VBD','VBN','VBP','VBZ']
#List of words that i felt if a tweet contained them, it would be innapropriate to make a meme about. 
#This is all the words i could think of/find on NY times headlines, so it is definately missing some
badWords=['abort','abuse','abusive', 'aids', 'bomb', 'burn','cancer', 'child', 'crime','dead','die','fire','gay', 'gang', 'grope', 'gun', 'hospital', 
          'kill','illegal','lgbt','lesbian','trans','illness', 'massacre', 'molest', 'murder','overdose','racism', 'racist', 'rape', 'rapist', 'refugee', 
          'rifle', 'sex', 'shoot','shot','scandal','slaughter','covid', 'stab','starve','starving','suffocate','suffocating', 'suspect','toxic', 'terror','Uvalde','victim', 
          'violence', 'weapon']

#Gets all tweets from NYT after(not including) the tweet ID passed in.
#Used to that if you save the latest tweet ID you can re-run this without hardcoding a new ID
def getTweets(sinceId):
    tweetIds=client.get_users_tweets(id=nytimesid,exclude=['retweets','replies'],user_auth=True,since_id=sinceId,max_results =20,tweet_fields='lang')
    return tweetIds.data
#Gets a singular tweet with the given ID, mainly used for debugging
def getTweetFromId(tweetId):
    return client.get_tweet(id=tweetId,user_auth=True,tweet_fields='lang')
#Checks the given tweet input and skips if either tweet is not in english or contains one of the banned words from above
def precheck(input):
    if input.lang != 'en':
        print('TweetId: '+str(input.id)+' is not English\n')
        return True
    inputStripped=input.text.strip().lower()
    for word in badWords:
        if word in inputStripped:
            print('TweetId: '+str(input.id)+' contains banned words\n')
            return True
#When given a word, tries to combine it with Morbius in the best possible way
#Rules:
#If it is a proper noun(E.G. name) changes it to Morbius and exits
#If it is a word where the stem of the word can be cleanly removed, swaps the stem for morb or Morb if it is capitalized
#   Example:
#   Kicking -> Kick + ing -> Morb + ing = Morbing
#If the stem cannot be cleanly removed OR the stem is the entire word, swaps the first 4 characters for morb or Morb. This logic can be much cleaner than what i have.
#   Example:
#   Complicates -> Comply + icates -> Comply not in Complicates-> ~~Comp~~licates -> Morb + licates = Morblicates
def morbWord(word):
    lst = LancasterStemmer()
    if word[1]=='NNP':
        return "Morbius"
    if word[0].isupper():
        newWord=word.replace(lst.stem(word).capitalize(),"Morb")
        if newWord=="Morb" or newWord==word:
            newWord="Morb" + word[4:]
    else:
        newWord=word.replace(lst.stem(word),"morb")
        if newWord=="morb" or newWord==word:
            newWord="morb" + word[4:]
    return newWord
#Breaks sentence into tokens, then runs morbWord on a random selection of words in the sentence.
#Then inserts the morbed word back into the origional sentence
#Example:
#   Input: I went fishing with my Dad
#   Output: I went morbing with my Morbius
def morbSent(input):
    tokenFiltered=tokenizeSentence(input)
    tokenSent= word_tokenize(input)
    nums=sample(range(len(tokenFiltered)),math.floor(len(tokenFiltered)/4))
    for i in range(len(nums)):
        tuple=tokenFiltered[nums[i]][0]
        fullTuple=tokenFiltered[nums[i]]
        morbedWord=morbWord(fullTuple)              
        tokenSent[tokenSent.index(tuple)]=morbedWord
    return tokenSent
# Tokenizes the sentence, then removes all stop words(the, a, an) and punctuation(.,!,?).
# Then returns a list of only the nouns and the verbs/adverbs, along with their type
# Example:
#   Input: I went fishing with my Dad, and we caught a nice big fish to eat.
#   Output: [('went', 'VBD'), ('fishing', 'VBG'), ('Dad', 'NNP'), ('caught', 'NN'), ('nice', 'RB'), ('fish', 'NN'), ('eat', 'NN')
def tokenizeSentence(input):
     stop = set(stopwords.words('english') + list(string.punctuation)+list("—"))
     newSent=nltk.pos_tag([i for i in word_tokenize(input) if i not in stop])
     filteredSent=[tup for tup in newSent if tup[1] in goodParts]
     return filteredSent
 
#Posts the updated string to Twitter using the account information provided above, in reply to the ID of the tweet that it is changing
def postToTwitter(morbedString,replyId):
    client.create_tweet(text=morbedString,in_reply_to_tweet_id =replyId)
    return "Posting Tweet " + morbedString

#Runs the program.
#Checks twitter for all tweets posted after id on the NYT twitter, then collects them all, and if they dont contain any bad words it modifys the sentence.
#It then posts the reply to twitter underneath the tweet it is modifying. Once it finishes all the tweets it saves the lastest tweet ID and sleeps for 15 minutes for more tweets to be created.
#There is additional logic in here for cleaning up sentences, mainly re-attaching "'s" to words, removing links, and replacing any instances of "Morbius Morbius" with "Micheal Morbius" to make tweets look better.
#Once started this can be left alone to run indefinetly 
def run():
    count=0
    id=1534374666562850817
    while True:
        print("Current Starting Id: "+str(id)+"\n")
        tweetList=getTweets(id)
        if tweetList:
            id=tweetList[0].id
            for tweet in tweetList:
                if not precheck(tweet):
                    count+=1
                    tweetText=tweet.text
                    httpRemoved = tweetText.split(seperator, 1)[0]
                    morbedString=(" ".join(morbSent(httpRemoved))).replace(" 's", "'s").replace(" .", ".").replace(" ,", ",")
                    morbedString=morbedString.replace("Morbius Morbius", "Micheal Morbius")
                    print('Replying to: '+str(tweet.id))
                    print('Reply Text: '+morbedString+'\n')
                    #print(postToTwitter(morbedString,tweet.id))
            print("Morbed "+str(count)+" Tweets so far")
        else:
            print('No new Tweets, sleeping for 15 minutes\n')
            time.sleep(900)
#Kicks off the script        
run()