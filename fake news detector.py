#!/usr/bin/env python
# coding: utf-8

# In[34]:


get_ipython().system('pip install textblob')
get_ipython().system('pip install newsapi-python')


# In[35]:


from textblob import TextBlob
from newsapi import NewsApiClient
import requests

# Replace YOUR_API_KEY with your actual API key
newsapi = NewsApiClient(api_key='55778ce7c2c5477b9a92d968ef50ec51')

#Get sentiment score for the article using TextBlob
def get_sentiment(url):
    response = requests.get(url)
    article = response.text
    blob = TextBlob(article)
    sentiment_score = blob.sentiment.polarity
    return sentiment_score

#get list of articles for a given source from NewsAPI

def get_articles(source):
    newsapi = NewsApiClient(api_key = '55778ce7c2c5477b9a92d968ef50ec51')
    top_headlines = newsapi.get_top_headlines(sources=source)
    articles = top_headlines['articles']
    return articles

#get average sentiment score for articles from a given source

def get_average_sentiment(source):
    articles = get_articles(source)
    if len(articles) == 0:
        print('No articles found for this source.')
        return 0
    total_sentiment = 0
    count = 0
    for article in articles:
        total_sentiment += get_sentiment(article['url'])
        count += 1
    average_sentiment = total_sentiment/len(articles)
    return average_sentiment

# determine if the website is biased or not
def is_biased(source):
    left_sources = ['cnn', 'msnbc', 'nytimes', 'washingtonpost', 'huffpost']
    right_sources = ['foxnews', 'breitbart', 'nypost', 'wsj']
    average_sentiment = get_average_sentiment(source)
    if average_sentiment > 0:
        print('This website has a positive bias.')
        return True
    elif average_sentiment < 0:
        print('This website has a negative bias.')
        return True
    else:
        print('This website is unbiased.')
        return False

url = input("Enter a website URL:")
source = url.split('.')[1]
is_biased(source)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Increase timeout to 60 seconds
response = requests.get(url, headers=headers, timeout=60)




#     #get the text contect of the article
#     content = newsapi.get_everything(q = url, language='en')['articles'][0]['content']
#     #analyze the sentiment of the content using textblob
#     blob = TextBlob(content)
#     return blob.sentiment.polarity

# #Promt the user for a website URL
# url = input('Enter a website URL:')

# #get 10 articles from the website
# articles = newsapi.get_everything(q=url, language='en', page_size = 10)['articles']

# #calculate the average sentiment score for the articles
# total_sentiment = 0
# count = 0
# for article in articles:
#     if 'url' in article:
#         total_sentiment += get_sentiment(article['url'])
#         count += 1
# average_sentiment = total_sentiment / len(articles)

# #determine if the website is biased or not
# if average_sentiment > 0.1:
#     print('This website is biased towards positive sentiment')
# elif average_sentiment < 0.1:
#     print('This website is biased towards negative sentiment')
# else: 
#     print('This website is not biased')
    
    


# In[ ]:




