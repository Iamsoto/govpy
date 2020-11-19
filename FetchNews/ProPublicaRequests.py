import requests
import os
import json

from Constants import ProPublicaFileLocation, Debugging, houseMembersURL

"""
	A class to handle the pro publica API
"""
class ProPublicaRequest(object):
	"""
		INIT

	params: 
		None
	"""
	def __init__(self):
		self.ProPublicaAPIKey = None

	def get_key(self ):
		key = ''
		with open(ProPublicaFileLocation(), 'r') as f:
			key = f.read()
			key = key.strip('\n').strip()
		if not key:
			raise ValueError("Error Processing ProPublica.txt")

		os.environ['ProPublicaAPIKey'] = key
		return key 


	def authenticationHeaders(self):
		ApiKey = self.get_key()
		return {'X-API-Key': ApiKey}

	"""
	Retreive house members

	params:
		None
	return:
		list dict members_list: A list of dictionaries representing the house members 

	"""
	def houseMembers(self):
		url = houseMembersURL()
		headers = self.authenticationHeaders()

		r = requests.get(url, headers=headers)
		r.raise_for_status()

		json_dict = json.loads(r.text)
		members_list =  []
		try: 
			members_list = json_dict["results"][0]["members"]
		except Exception as e:
			raise Exception("Error processing JSON" + str(e))

		return members_list



