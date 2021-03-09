

#using scraper_tweepy.py

from scraper_tweepy import scraper_tweepy

dict=['volkswagen','polo','golf','passat','tiguan']
output='tweets.csv'
begin_date='2021-03-06'

scraper_tweepy(dict,output,begin_date)