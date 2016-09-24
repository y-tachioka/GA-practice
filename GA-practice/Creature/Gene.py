# -*- coding: utf-8 -*-

########################################################################
#Gene Class
########################################################################

class Gene():
	def __init__(self):
		self.sequences = [] #0~7 0~3=x 4~7=y
		self.v = None

	def makeCoordinate(self,_number,_generation):#座標値入れる
		binary = 1
		x = 0
		for i in range(0,4):
			x = x + (self.sequences[i]*binary)
			binary = binary*2
		x = x + (30*(_number))#位置調整

		binary = 1
		y = 0
		for j in range(4,8):
			y = y + (self.sequences[j]*binary)
			binary = binary*2
		y = y -(30*(_generation))#位置調整
		self.v = [x,y,0]