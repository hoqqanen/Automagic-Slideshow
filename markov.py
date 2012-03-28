"""Usage:
Call python markov.py tag1 tag2 tag3 ....
Options forthcoming.
"""

import flickr
import urllib
import Image
import time
import datetime
import sys
import os
from random import choice, shuffle

time_now = datetime.datetime.now()
folder_name = time_now.strftime('%d-%m,%H-%M-%S')

tags = []
alltags = set(tags)
def load_photo(url):
	file, mime = urllib.urlretrieve(url.encode('utf-8'))
	photo = Image.open(file)
	return photo
	
def show_pic(tags, idx):
	photos = flickr.photos_search(tags=tags,per_page=50)
	ppp = choice(photos)
	u = ppp.getURL(size='Medium',urlType='source')
	ph = load_photo(u)
	#ph.show()
	ph.save("pictures/"+folder_name+"/"+str(idx)+".jpg","JPEG")
	newtagset = tags[1:]
	newtags = list(set(ppp.tags)-alltags)
	if len(newtags)==0:
		print 'done'
	newtagset.append(choice(newtags).text.encode('utf-8'))
	return newtagset


def main(*tag_list):
	os.mkdir('pictures/'+folder_name)
	f = open('pictures/'+folder_name+'/log.txt','w')
	tags = list(tag_list[1:])
	f.write('0: '+str(tags)+'\n')
	alltags = set(tags)
	for i in range(20):
		tags = show_pic(tags, i)
		alltags = alltags | set(tags)
		f.write(str(i+1)+': '+str(tags)+'\n')
		#print alltags
		#time.sleep(.1)
	f.close()
	
if __name__ == '__main__':
	sys.exit(main(*sys.argv))