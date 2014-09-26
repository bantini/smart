#http://stackoverflow.com/questions/10894692/python-outfile-to-another-text-file-if-exceed-certain-file-size

import os
import sys
from os.path import join
from time import strftime,gmtime

class RotatingFile(object):
	
	filename = "Default"

	def __init__(self, directory='../data', filename='foo', max_files=sys.maxint, max_file_size=50,search_term="foo"):
		self.ii = 1
		self.directory, self.filename      = directory, filename
		self.max_file_size, self.max_files = max_file_size, max_files
		self.finished, self.fh             = False, None
		self.open()

	def rotate(self):
		"""Rotate the file, if necessary"""
		if (os.stat(self.filename_template).st_size>self.max_file_size):
		    self.close()
		    self.open()

	def open(self):
		RotatingFile.filename = self.search_term+strftime("%m%d%Y%S%H%M",gmtime())
		self.fh = open(join(self.directory,RotatingFile.filename), 'w')

	def write(self, text=""):
		self.fh.write(text)
		self.fh.flush()
		self.rotate()

	def close(self):
		self.fh.close()

	@property
	def filename_template(self):
		return RotatingFile.filename