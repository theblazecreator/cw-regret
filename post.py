#!/usr/bin/python
import configparser, os, sys, time
from termcolor import colored
from twitter import *
config = configparser.ConfigParser()
config.read('creds.ini')

def login():
    twitter_access_key = config.get('Credentials', 'Twitter_Access_Key')
    twitter_access_secret = config.get('Credentials', 'Twitter_Access_Secret')
    twitter_consumer_key = config.get('Credentials', 'Twitter_Consumer_Key')
    twitter_consumer_secret = config.get('Credentials', 'Twitter_Access_Secret')
    if twitter_access_key == "replace_me" or twitter_access_secret == "replace_me" or twitter_consumer_key == "replace_me" or twitter_consumer_secret == "replace_me":
	       print(colored("read the docs, idiot", 'red'))
           os.system("pause>nul")
           sys.exit()
    try:
        twitter = Twitter(
	auth = OAuth(config["twitter_access_key"], config["twitter_access_secret"], config["twitter_consumer_key"], config["twitter_consumer_secret"]))
game_name = input("Please enter the game name (Use normal scene writing, do not include a dash or the release group):")
release_group = input("Please enter the short form of the release group (do not include a dash): ")
thread_link = input("Please enter the discussion thread link:")