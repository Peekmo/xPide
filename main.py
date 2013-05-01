###########################################################
#### Main.py
#### Created : 04-29-2013
#### Last Update : 04-29-2013
#### By Peekmo
###########################################################

#! /usr/bin/python2
#-*-coding: utf-8 -*-

from PyQt4.QtGui import *
from mainwindow import *
import sys
import os

def main(args):
	a = QApplication(args)
	window = MainWindow()

	# Definition du stylesheet
	fichier = QFile("default.qss")
	fichier.open(QFile.ReadOnly)
	style = QLatin1String(fichier.readAll())
	a.setStyleSheet(style)

	window.show()
	r = a.exec_()
	return r

if __name__ =="__main__":
	main(sys.argv)