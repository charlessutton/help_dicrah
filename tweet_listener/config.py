  #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 09:30:52 2018

@author: Michi
@contributors: Alex, Ed
"""

#################################################
#################################################

# Configuration file for the code 'StreamListener_mm.py'

#################################################
#################################################


######
# VARIABLES GLOBALES
######


# Gestion des fichiers locaux
credentialsFile = 'Credentials.csv'
# Modif. tirée du code d'Alex, pour ne pas montrer les credentials
# sur le fichier et les rendre publiques sur GitHub. Il faut garder le
# fichier 'Credentials.csv' sur la machine locale et ne pas push sur GitHub (Ed)



######
# Récupération des credentials twitter
######
credentials = open(credentialsFile, 'r') 
CONSUMER_KEY = credentials.readline().strip()
CONSUMER_SECRET = credentials.readline().strip()
ACCESS_TOKEN = credentials.readline().strip()
ACCESS_TOKEN_SECRET = credentials.readline().strip()
credentials.close()




######
#  Input parameters - edit these !
######


# Query name
query_fname = 'prova' # Name of the output jsonl file in the folder Streams/



#  If true, the code will print some updates while running
Verbose = True


#  hashtags or keywords to filter the stream. Must be a list of strings
# Liste proposée à partir du dictionnaire termes bannis Android et quelque
# hashtags populaires sur racisme. Elle peut être modifiée à tout moment,
# car les nouvelles recherches font un append sur les données déjà scrappées (Ed)

#query = ['babouin', 'babtou', 'bamboula', 'banania', 'bicot','bicotte', 'blanc-bec', 'boche', 'bosnioule', 'boucaque', 'bougnoul','bougnoule', 'boukak', 'bounioul', 'bounioule', 'bridé', 'bridée', 'caillera', 'caldoche', 'chinetoque', 'chinoir', 'chintoque','chleuh', 'crépu', 'crepu', 'crouille', 'doryphore','enturbanné', 'fatma', 'frisé', 'gnoul', 'gnoule','israélite', 'krèle', 'krele', 'macaca', 'météque', 'meteque', 'météques', 'meteques', 'mouloud', 'moulouds', 'mulâtre', 'mulatre','nègre', 'negre', 'négritude', 'negritude', 'négro', 'negro', 'néonazi','nazi', 'niaquoué', 'noiraud', 'portos', 'racaille','raton', 'rital', 'ritals', 'rosbif', 'swastika','toubab', 'youd', 'youpin', 'youpine', 'youpins', '#Racisme','#RacismeOrdinaire', 'raciste'] # a list of strings

query = ['#TuesdayThoughts']

# Language to filter the stream.
languages = ['en'] # ex. ['fr']

#  Time limit in seconds.  Must be an integer or None if you don't want any 
time_limit = 30 # an int or None 



# If follow_conversations = True, the code will check if a tweet is a reply; if so, it will retrieve the conversation
#
# max_tweets_conv is the max number of tweets fetched 

follow_conversations = True



# if get_user_tweets = True, the code will save the first n_tweets
# of the first n_pages of each new user's timeline.

get_user_tweets = False
n_tweets_user=20
n_pages_user=1






#####
# Example of output
#####

# query_fname = 'ex_query'
# data_dir = my_dir/
# query = ['#9Mai']
# languages = ['fr']
# time_limit = 10
# get_user_tweets = True
# n_tweets=50
# n_pages=4

# this will output:
# - the file 'Streams/stream_ex_query.jsonl' with all tweets containing the hashtag #9mai . Each line(~tweet) is a json.
# - a file 'Users/user_timeline_<username>.jsonl' for every different <usename> that tweeted about your query.
#   In this case we collected 50 tweets * 4 pages  = 200 tweets for each user.
# - a file 'Users/stream_ex_query_users_list.txt' with a list of the usernames whose tweets we collected
