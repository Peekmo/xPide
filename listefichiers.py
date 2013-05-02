###########################################################
#### listefichiers.py
#### Created : 05-01-2013
#### Last Update : 05-01-2013
#### Toute reproduction ou diffusion a des fins commerciales
#### est strictement interdite.
####
#### By Peekmo
###########################################################

#! /usr/bin/python
#-*-coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
from content import *

class ListeFichiers(QStandardItemModel):
	def __init__(self):
		QStandardItemModel.__init__(self)
		self.fichiers = []

	def addFile(self, content):
		self.fichiers.append(content)
		self.appendRow(QStandardItem(content.getNom()))

	def refreshNames(self):
		for i, f in enumerate(self.fichiers):
			self.item(i).setText(f.getNom())


