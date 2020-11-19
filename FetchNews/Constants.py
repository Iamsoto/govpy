import os

def Debugging():
	return True

def ProPublicaFileLocation():
	return "{}/{}".format(os.path.dirname(os.path.realpath(__file__)), 'ProPublica.txt')

def ProPublicaBaseURL():
	return 'https://api.propublica.org/congress/v1/'

# TODO: Update every election
def houseMembersURL(congress = '116'):
	return "https://api.propublica.org/congress/v1/{}/house/members.json".format(str(congress))

def senateMembersURL(congress = '116'):
	return "https://api.propublica.org/congress/v1/{}/senate/members.json".format(str(congress))

"""
	News URLS
"""
def ReutersURL():
	return "https://www.reuters.com/politics"