# -*- coding: utf-8 -*-
import rhinoscriptsyntax as rs
import Rhino

########################################################################
#Phenotype Class
########################################################################

class Phenotype():
	def __init__(self):
		self.genes = [] #genes in 8
		self.parents = [] #Phenotype 2
		self.number = -1
		self.generation = 0
		#評価---------------------------
		self.length = -1

	def setLength(self):
		pts = []
		for gene in self.genes:
			pts.append(gene.v)
		pts = rs.coerce3dpointlist(pts, True)
		curve = Rhino.Geometry.Polyline(pts)
		curve = curve.ToNurbsCurve()
		self.length = rs.CurveLength(curve)
		print "Curve length:", self.length


