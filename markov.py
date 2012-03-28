"""Usage:
Call python markov.py tag1 tag2 tag3 ....
Options forthcoming.
"""

import flickr
import urllib
import Image
import time
import sys
from random import choice, shuffle

tags = []
alltags = set(tags)
def load_photo(url):
	file, mime = urllib.urlretrieve(url.encode('utf-8'))
	photo = Image.open(file)
	return photo
	
def show_pic(tags):
	photos = flickr.photos_search(tags=tags,per_page=50)
	ppp = choice(photos)
	u = ppp.getURL(size='Medium',urlType='source')
	print u
	ph = load_photo(u)
	ph.show()
	newtagset = tags[1:]
	newtags = list(set(ppp.tags)-alltags)
	if len(newtags)==0:
		print 'done'
	newtagset.append(choice(newtags).text.encode('utf-8'))
	return newtagset


def main(*tag_list):
	print tag_list[1:]
	tags = list(tag_list[1:])
	alltags = set(tags)
	for i in range(10):
		tags = show_pic(tags)
		alltags = alltags | set(tags)
		print tags
		#print alltags
		time.sleep(.1)
	
if __name__ == '__main__':
	sys.exit(main(*sys.argv))