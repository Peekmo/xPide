###########################################################
#### content.py
#### Created : 04-29-2013
#### Last Update : 04-30-2013
#### Toute reproduction ou diffusion a des fins commerciales
#### est strictement interdite.
####
#### By Peekmo
###########################################################

#! /usr/bin/python
#-*-coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import os
import sys

from linenumber import *

class Content(QPlainTextEdit):
	def __init__(self, parent):
		QPlainTextEdit.__init__(self, parent)
		self.lineNumber = LineNumber(self)

		self.connect(self, SIGNAL("blockCountChanged(int)"), self.updateLargeurLigne)
		self.connect(self, SIGNAL("updateRequest(QRect, int)"), self.updateNumeroLigne)
		self.connect(self, SIGNAL("cursorPositionChanged()"), self.highlighting)

		self.updateLargeurLigne(0)
		self.highlighting()

	def largeurLigne(self):
		digits = 1
		liste = []
		liste.append(1)
		liste.append(self.blockCount())
		maxi = max(liste)

		while maxi >= 10:
			maxi /= 10
			digits += 1

		space = 15 + self.fontMetrics().width('9') * digits

		return space

	def numeroLignePaint(self, event):
		painter = QPainter(self.lineNumber)
		rect = event.rect()
		painter.fillRect(rect, QColor("#272822"))

		block = self.firstVisibleBlock()
		blockNumber = block.blockNumber()
		top = int(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
		bottom = top + int(self.blockBoundingRect(block).height())

		# Merci John
		ligneActuelle = self.document().findBlock(self.textCursor().position()).blockNumber()

		while block.isValid() and top <= event.rect().bottom():
			if block.isVisible() and bottom >= event.rect().top():
				if ligneActuelle == blockNumber:
					painter.fillRect(0, top, self.lineNumber.width(), self.fontMetrics().height(), QColor("#393928"))

				number = QString.number(blockNumber + 1)
				painter.setPen(QPen(Qt.white))
				painter.drawText(0, top, self.lineNumber.width(), self.fontMetrics().height(), Qt.AlignCenter, number)

			block = block.next()
			top = bottom
			bottom = top + int(self.blockBoundingRect(block).height())
			blockNumber += 1

	def updateNumeroLigne(self, rect, pixels):
		if pixels:
			self.lineNumber.scroll(0, pixels)
		else:
			self.lineNumber.update(0, rect.y(), self.lineNumber.width(), rect.height())

		if rect.contains(self.viewport().rect()):
			self.updateLargeurLigne(0)

	def updateLargeurLigne(self, w):
		self.setViewportMargins(self.largeurLigne(), 0, 0, 0)

	def highlighting(self):
		extraSelections = []

		if not self.isReadOnly():
			selection = QTextEdit.ExtraSelection()
			lineColor = QColor("#393928")

			selection.format.setBackground(lineColor)
			selection.format.setProperty(QTextFormat.FullWidthSelection, True)
			selection.cursor = self.textCursor()
			selection.cursor.clearSelection()
			extraSelections.append(selection)

		self.setExtraSelections(extraSelections)

	def resizeEvent(self, event):
		QPlainTextEdit.resizeEvent(self, event)

		cr = self.contentsRect()
		self.lineNumber.setGeometry(QRect(cr.left(), cr.top(), self.largeurLigne(), cr.height()))
