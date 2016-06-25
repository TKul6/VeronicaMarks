import os
import itertools
from Bookmark import Bookmark;
class Marker:


	def __init__(self,marks):

		self.__marks = {}

		for mark in marks:
			self.__marks[mark] = []

	def mark_file(self,path):
		with open(path) as file:
			lines = file.readlines()
			line_index = 1;
			for line in lines:
				for mark in self.__marks.keys():
					mark_index = line.find(mark);
					if mark_index >=0:
						self.__marks[mark].append(Bookmark(mark,path,line_index,mark_index) )
				line_index+= 1;
		
	def mark_directory(self,path):
		if(os.path.isdir(path)):
			for entry in os.listdir(path):
				childPath = os.path.join(path,entry)
				if(os.path.isdir(childPath)):
					self.__mark_directory(childPath)
				else:
					self.__mark_file(childPath);
		else:
			print "Direcotry " + path + " does not exsits";

	def add_mark(self, mark):
		self.__marks[mark] = [];

	def remove_mark(self,mark):
		del self.__marks[mark]

	def clear_marks(self):
		self.__marks.clear()

	def print_marks(self):
		print self.__marks.keys()

	def print_bookmarks(self):
		for bookmark_list in self.__marks.values():
			for bookmark in bookmark_list:
				print bookmark



