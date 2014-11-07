# Import SQLAlchemy stuff
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Post, Base

# Import PRAW
import praw
import time

# Prelim setup
engine = create_engine('sqlite:///praw.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Handle ALL Reddit Scraping
##########

# Reddit Setup
r = praw.Reddit('Post Databasing Program')
visited = []

keywords = [
'program design',
'praw',
'study',
'class',
'productivity',
'module',
'framework',
'agency',
'pygame',
'tkinter',
'python',
'C',
'Unity',
'programming standard'
]

# Declare Subs to follow
pythonsub = r.get_subreddit('python')

# Main loop per sub
for submission in pythonsub.get_hot(limit=10):
	submission.replace_more_comments(limit=15, threshold=0)
	title = submission.title
	print('Title Found: %s') % title
	post = submission.selftext.lower()
	print('Post Found')
	link = submission.url
	print('Link Found: %s') % link
	parsed = praw.helpers.flatten_tree(submission.comments)
	commentlist = []
	print('Processing Comments...')
	for comment in parsed:
		commentlist.append(comment.body)
		commentlist.append('<===**===>')
	comments = ''.join(commentlist)
	print('Comments Processed')
	new_post = Post(title=title, post=post, comments=comments, link=link)
	session.add(new_post)
	session.commit()
