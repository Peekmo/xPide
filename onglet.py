###########################################################
#### onglet.py
#### Created : 04-29-2013
#### Last Update : 04-29-2013
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

class Onglet(QWidget):
	def __init__(self, p):
		QWidget.__init__(self)
		self.parent = p
		self.nom = QString("Nouveau")
		self.lastSave = True

		self.setContentsMargins(0,0,0,0)

		self.content = Content(self)
		self.content.setTabStopWidth(25)
		self.content.setFont(QFont("Inconsolata"))

		self.layout = QVBoxLayout()
		self.layout.setMargin(0)
		self.layout.addWidget(self.content)
		self.layout.setMargin(0)
		self.layout.setSpacing(0)

		self.setLayout(self.layout)

		self.connect(self.content, SIGNAL("textChanged()"), self.unSave)

	def unSave(self):
		if self.lastSave:
			self.lastSave = False
			self.nom = "* "+self.nom
			self.parent.majTabName()

	def save(self):
		if not self.lastSave:
			self.lastSave = True
			self.nom = self.nom.split("*")[1][1:]
			self.parent.majTabName()

	def getNom(self):
		return self.nom 