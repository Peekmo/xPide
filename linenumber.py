###########################################################
#### linenumber.py
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

class LineNumber(QWidget):
	def __init__(self, c):
		QWidget.__init__(self, c)
		self.content = c

	def sizeHint(self):
		return QSize(self.content.largeurLigne(), 0)

	def paintEvent(self, event):
		self.content.numeroLignePaint(event)