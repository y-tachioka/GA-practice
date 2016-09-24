# -*- coding: utf-8 -*-
import random as rnd
import rhinoscriptsyntax as rs
import scriptcontext

from Gene import Gene
from Phenotype import Phenotype

class Ecosystem():
	def __init__(self):
		self.phenotypes = []
		self.generation = 0

	def makeEcosystem(self):
		#-00
		Egeneration = rs.GetInteger("何世代進化させますか")
		#-01
		self.firstSeed()
		#-02
		while (self.generation != Egeneration):
			self.generation += 1
			
			#-02_1
			tmpParents = self.selParents()
			#-02_2
			self.nextSeed(tmpParents)

			print "next generation!"
			scriptcontext.escape_test()
		#-03
		self.draw()

	#######################################################
	#-01
	#phenotype.genes
	#gene.sequences
	#gene.v
	#######################################################
	def firstSeed(self):
		for i in range(10):
			phenotype = Phenotype()
			for j in range(8):
				gene = Gene()
				for k in range(8):
					gene.sequences.append(rnd.randint(0,1))
				gene.makeCoordinate(i,self.generation)
				phenotype.genes.append(gene)
			phenotype.number = i
			phenotype.generation = self.generation
			phenotype.setLength()
			self.phenotypes.append(phenotype)

	#######################################################
	#-02_1
	#######################################################
	def selParents(self):
		pass

	#######################################################
	#-02_2
	#######################################################
	def nextSeed(self,tmpParents):
		pass

	#######################################################
	#-03
	#######################################################
	def draw(self):
		for phenotype in self.phenotypes:
			pts = []
			for gene in phenotype.genes:
				pts.append(gene.v)
			rs.AddPolyline(pts)





