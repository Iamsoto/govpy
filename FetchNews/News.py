import os
from Utility import RandomStringManager

class NewsScrapper(object):
	"""
		INIT NEwsScrapper
	"""
	def __init__(self, main_url, file_header):
		self.main_url = main_url
		self.file_header = file_header
		self.file_manager_name = "file_manager"
		self.article_urls = []
		self.dir_path = os.path.dirname(os.path.realpath(__file__))
		if self.dir_path[-1] != "/":
			self.dir_path  = self.dir_path + "/"

	"""
		implement in base class
	"""
	def get_articles(self):
		pass

	"""
		implement in base class
	"""
	def get_article_text(self, url):
		pass
	
	"""
		Retreive list of local files written in file manager

		params:
			None
		return:
			list files, a list of file paths
	"""
	def get_local_files(self):
		files = []
		file_manager_path = "{}{}{}.txt".format(self.dir_path, self.file_header, self.file_manager_name)
		if not os.path.exists(file_manager_path):
			raise OSError("Cannot locate file {} deleting 0 files".format(file_manager_path))
		else: 
			# Each line should represent a file. Important: split lines
			lines = open(file_manager_path, "r").read().splitlines()
			for line in lines:
				files.append(line)

		return files

	"""
		Remove all local files written in file manager

		params:
			None
		return:
			None
	"""
	def remove_local_files(self):
		files = []
		try:
			files = self.get_local_files()
		except OSError as e:
			print("Exception caught while retreiving local files {}".format(str(e)))
			return None
		for file in files:
			try:
				os.remove(file)
			except OSError as e:
				print("Error removing a file: {}".format(str(e)))

		# Lastly, try to remove the file manager
		try:
			file_manager_path = "{}{}{}.txt".format(self.dir_path, self.file_header, self.file_manager_name)
			os.remove(file_manager_path)
		except OSError as e:
			print("Error removing file manager: {}".str(e))

		return None



	"""
		Download all articles to local filesotrage in self.article_urls
		Does not overwrite file if it exists
		
		params: 
			None
		return:
			None 
	"""
	def download_articles(self):
		# must call get_articles first
		

		if not bool(len(self.article_urls)):
			self.get_articles()

		file_manager_path = "{}{}{}.txt".format(self.dir_path, self.file_header, self.file_manager_name)

		rsm = RandomStringManager()
		for article in self.article_urls:
			path = "{}{}{}.txt".format(self.dir_path, self.file_header, rsm.getString(10))
			if os.path.exists(path):
				raise OSError("File {} already exists".format(path))
			else: 
				# Write contents of article into a local file
				with open(path, "w+") as f:
					# First line must be url
					f.write("{}\n".format(article))
					paragraphs = self.get_article_text(article)
					for paragraph in paragraphs:
						f.write("{}\n".format(paragraph))

				# Add local file location to  our management file 
				with open(file_manager_path, "a+") as manager:
					manager.write("{}\n".format(path))
