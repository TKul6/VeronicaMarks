import os

class Marker:
	def __init__(self,marks):
		self.marks = marks

	def mark_file(self,path):
		print "	File Name:" + path
		
	def mark_directory(self,path):
		if(os.path.isdir(path)):
			for entry in os.listdir(path):
				childPath = os.path.join(path,entry)
				if(os.path.isdir(childPath)):
					self.mark_directory(childPath)
				else:
					self.mark_file(childPath);
		else:
			print "Direcotry " + path + " does not exsits";

	def add_mark(self, mark):
		self.marks.append(mark)

	def remove_mark(self,mark):
		self.marks.remove(mark)

	def clear_marks(self):
		self.marks = [];

	def print_marks(self):
		print self.marks



