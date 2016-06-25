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

