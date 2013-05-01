###########################################################
#### onglet.py
#### Created : 04-29-2013
#### Last Update : 04-29-2013
#### By Peekmo
###########################################################

#! /usr/bin/python
#-*-coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import os
import sys

from content import *

class Onglet(QWidget):
	def __init__(self, p):
		QWidget.__init__(self)
		self.parent = p
		self.nom = "Nouveau"
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