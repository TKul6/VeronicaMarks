class Bookmark:

	def __init__(self,mark,file_name,line,position):
		self.mark = mark
		self.file_name = file_name
		self.line = line
		self.position = position

	def __str__(self):
		return "[mark:{0}, filename: {1}, line number: {2}, position: {3}]".format(self.mark,self.file_name,self.line,self.position)
		





