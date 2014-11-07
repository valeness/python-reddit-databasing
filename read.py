from db import Post, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///praw.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

post = session.query(Post)

# Spacer
sp = ' | '

for post in post:
	id = str(post.id).zfill(2)
	title = post.title[:25]
	link = post.link[:25]
	print('%s %s %s %s %s') % (id, sp, title, sp, link)

query = raw_input(':>')
result = session.query(Post).filter(Post.id == query).one()

print('Title')
print(result.title)
