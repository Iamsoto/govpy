import requests
import os
from bs4 import BeautifulSoup
from News import NewsScrapper
from Constants import ReutersURL
#from HTMLParser import HTMLParseError


class ReutersScrapper(NewsScrapper):

	"""
		INIT Reuters Scrapper 

		params:
			None
		return:
			None
	"""
	def __init__(self):
		if not os.path.exists("{}/{}".format( os.path.dirname(os.path.realpath(__file__)), "Reuters_Downloads")):
			os.mkdir("{}/{}".format(os.path.dirname(os.path.realpath(__file__), "Reuters_Downloads")))
		
		super().__init__(ReutersURL(), "Reuters_Downloads/Reuters_Downloaded_File_")

	"""
		Retreive all text in a given Reuters article
		Note: 
			-First item is URL
			-Last item is Title

		params:
			str url: url of article to retreive text from
		return: 
			list paragraph_texts: list of texts, each text is a paragraph, position -1 is the title
	"""
	def get_article_text(self, url):
		paragraph_texts = []
		r1 = requests.get(url)
		page = r1.content
		soup1 = BeautifulSoup(page, "html.parser")
		div_content = soup1.find('div', class_ = "StandardArticleBody_body")
		paragraphs = div_content.find_all("p")
		for paragraph in paragraphs:
			paragraph_texts.append(paragraph.text)

		h1_content = soup1.find("h1", class_ = "ArticleHeader_headline")
		paragraph_texts.append(h1_content.text)

		return paragraph_texts
	
	"""
		Parse self.main_url to populate article_urls 
		
		
		params:
			None	
		return: 
			list article_urls: list of article urls
	"""
	def get_articles(self):
		article_url_dict = {}
		article_url_list = []		
		r1 = requests.get(self.main_url)
		coverpage = r1.content	
		soup1 = BeautifulSoup(coverpage, "html.parser")

		# Grab all header tags
		headline_tags = soup1.find_all('h2', class_ = 'FeedItemHeadline_headline')

		# Make sure results are showing, the site hasnt changed
		if not bool(len(headline_tags)):
			raise Exception("No headlines found when parsing Reuters")

		# Iterate over all headlines 
		for headline_tag in headline_tags:
			try:
				url = headline_tag.a['href']
			#TODO: I'm not sure what exceptions beautiful soup raises...
			except Exception:
				print("HTML parse error when retreiving Reuters article URLS")
				return None
			# Duplicate URLS are returned, for some reason, 
			# so we need to use a dictionary
			if url not in article_url_dict:
				article_url_dict[url] = 1

		# convert dictionary to a list
		for url in article_url_dict.keys():
			article_url_list.append(url)

		self.article_urls = article_url_list
		return article_url_list


