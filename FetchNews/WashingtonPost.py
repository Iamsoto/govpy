
import requests
from bs4 import BeautifulSoup

"""
Useful links: 
https://morioh.com/p/abf3d53739f8

https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Wash Post target URL: 
https://www.washingtonpost.com/politics/white-house/
"""

# Test 1: Give base URL, return article links
def get_article_links(url="https://www.washingtonpost.com/politics/white-house/"):
	r1 = requests.get(url)
	coverpage = r1.content	
	soup1 = BeautifulSoup(coverpage, "html.parser")

	# We're looking for the class div class = "story-headline"
	headline_divs = soup1.find_all('div', class_='story-headline')

	# This works :) 
	links = []
	for child in headline_divs:
		links.append(child.find('h2').find('a')['href'])
	return links 
	#return headline_divs[0].find('h2').find('a')['href']


def testing2():
	print(str(len(get_article_links())))

def testing():
	file_name = "WashPost_Headers.txt"
	with open(file_name, "w+")as f:
		children_of_first_story_headline_div = get_article_links()
		for child in children_of_first_story_headline_div:
			f.write("{}\n".format(str(child)))

testing2()
#testing()

#print(get_article_links().prettify())