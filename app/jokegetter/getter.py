import requests
import json
import praw
def get():
	with open('app/login/data.txt', 'r') as f:
		data = f.readlines()
	login_data = []
	for line in data:
		login_data.append(line.replace('\n', ''))
	reddit = praw.Reddit(client_id=login_data[0], \
                     client_secret=login_data[1], \
                     user_agent=login_data[2], \
                     username=login_data[3], \
                     password=login_data[4])
	subreddit = reddit.subreddit('Jokes')
	print('Today\'s jokes:')
	print()
	print('----------------')
	print()
	for submission in subreddit.new(limit=100):
		print(submission.title)
		print(submission.selftext)
		print()
		print('------------------')
		print()
