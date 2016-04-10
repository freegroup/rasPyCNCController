# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JogWidget/jogWidget.ui'
#
# Created: Sun Apr 10 09:55:37 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_joyWidget(object):
    def setupUi(self, joyWidget):
        joyWidget.setObjectName("joyWidget")
        joyWidget.resize(480, 320)
        self.fileLabel = QtGui.QLabel(joyWidget)
        self.fileLabel.setGeometry(QtCore.QRect(10, 10, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.fileLabel.setFont(font)
        self.fileLabel.setCursor(QtCore.Qt.UpArrowCursor)
        self.fileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fileLabel.setObjectName("fileLabel")
        self.posGroup = QtGui.QGroupBox(joyWidget)
        self.posGroup.setGeometry(QtCore.QRect(5, 50, 230, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.posGroup.setFont(font)
        self.posGroup.setObjectName("posGroup")
        self.xPosTxt = QtGui.QLineEdit(self.posGroup)
        self.xPosTxt.setGeometry(QtCore.QRect(10, 30, 70, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.xPosTxt.setFont(font)
        self.xPosTxt.setText("")
        self.xPosTxt.setReadOnly(True)
        self.xPosTxt.setObjectName("xPosTxt")
        self.yPosTxt = QtGui.QLineEdit(self.posGroup)
        self.yPosTxt.setGeometry(QtCore.QRect(80, 30, 70, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.yPosTxt.setFont(font)
        self.yPosTxt.setText("")
        self.yPosTxt.setReadOnly(True)
        self.yPosTxt.setObjectName("yPosTxt")
        self.zPosTxt = QtGui.QLineEdit(self.posGroup)
        self.zPosTxt.setGeometry(QtCore.QRect(150, 30, 70, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.zPosTxt.setFont(font)
        self.zPosTxt.setText("")
        self.zPosTxt.setReadOnly(True)
        self.zPosTxt.setObjectName("zPosTxt")
        self.BBOxGroup = QtGui.QGroupBox(joyWidget)
        self.BBOxGroup.setEnabled(True)
        self.BBOxGroup.setGeometry(QtCore.QRect(240, 50, 230, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BBOxGroup.setFont(font)
        self.BBOxGroup.setObjectName("BBOxGroup")
        self.xMinBBoxTxt = QtGui.QLineEdit(self.BBOxGroup)
        self.xMinBBoxTxt.setGeometry(QtCore.QRect(10, 30, 70, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.xMinBBoxTxt.setFont(font)
        self.xMinBBoxTxt.setText("")
        self.xMinBBoxTxt.setReadOnly(True)
        self.xMinBBoxTxt.setObjectName("xMinBBoxTxt")
        self.yMinBBoxTxt = QtGui.QLineEdit(self.BBOxGroup)
        self.yMinBBoxTxt.setGeometry(QtCore.QRect(80, 30, 70, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.yMinBBoxTxt.setFont(font)
        self.yMinBBoxTxt.setText("")
        self.yMinBBoxTxt.setReadOnly(True)
        self.yMinBBoxTxt.setObjectName("yMinBBoxTxt")
        self.zMinBBoxTxt = QtGui.QLineEdit(self.BBOxGroup)
        self.zMinBBoxTxt.setGeometry(QtCore.QRect(150, 30, 70, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.zMinBBoxTxt.setFont(font)
        self.zMinBBoxTxt.setText("")
        self.zMinBBoxTxt.setReadOnly(True)
        self.zMinBBoxTxt.setObjectName("zMinBBoxTxt")
        self.xMaxBBoxTxt = QtGui.QLineEdit(self.BBOxGroup)
        self.xMaxBBoxTxt.setGeometry(QtCore.QRect(10, 70, 70, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.xMaxBBoxTxt.setFont(font)
        self.xMaxBBoxTxt.setText("")
        self.xMaxBBoxTxt.setReadOnly(True)
        self.xMaxBBoxTxt.setObjectName("xMaxBBoxTxt")
        self.yMaxBBoxTxt = QtGui.QLineEdit(self.BBOxGroup)
        self.yMaxBBoxTxt.setGeometry(QtCore.QRect(80, 70, 70, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.yMaxBBoxTxt.setFont(font)
        self.yMaxBBoxTxt.setText("")
        self.yMaxBBoxTxt.setReadOnly(True)
        self.yMaxBBoxTxt.setObjectName("yMaxBBoxTxt")
        self.zMaxBBoxTxt = QtGui.QLineEdit(self.BBOxGroup)
        self.zMaxBBoxTxt.setGeometry(QtCore.QRect(150, 70, 70, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.zMaxBBoxTxt.setFont(font)
        self.zMaxBBoxTxt.setText("")
        self.zMaxBBoxTxt.setReadOnly(True)
        self.zMaxBBoxTxt.setObjectName("zMaxBBoxTxt")
        self.estTimeGroup = QtGui.QGroupBox(joyWidget)
        self.estTimeGroup.setGeometry(QtCore.QRect(240, 165, 230, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.estTimeGroup.setFont(font)
        self.estTimeGroup.setObjectName("estTimeGroup")
        self.estTimeTxt = QtGui.QLineEdit(self.estTimeGroup)
        self.estTimeTxt.setGeometry(QtCore.QRect(10, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.estTimeTxt.setFont(font)
        self.estTimeTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.estTimeTxt.setReadOnly(True)
        self.estTimeTxt.setObjectName("estTimeTxt")
        self.label = QtGui.QLabel(joyWidget)
        self.label.setGeometry(QtCore.QRect(10, 130, 221, 101))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.RunButton = QtGui.QPushButton(joyWidget)
        self.RunButton.setGeometry(QtCore.QRect(5, 255, 231, 61))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(27)
        font.setWeight(75)
        font.setBold(True)
        self.RunButton.setFont(font)
        self.RunButton.setObjectName("RunButton")
        self.LoadButton = QtGui.QPushButton(joyWidget)
        self.LoadButton.setGeometry(QtCore.QRect(245, 255, 231, 61))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(27)
        font.setWeight(75)
        font.setBold(True)
        self.LoadButton.setFont(font)
        self.LoadButton.setObjectName("LoadButton")
        self.exitButton = QtGui.QPushButton(joyWidget)
        self.exitButton.setGeometry(QtCore.QRect(436, 5, 41, 41))
        self.exitButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/x_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exitButton.setIcon(icon)
        self.exitButton.setIconSize(QtCore.QSize(24, 24))
        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(joyWidget)
        QtCore.QMetaObject.connectSlotsByName(joyWidget)

    def retranslateUi(self, joyWidget):
        joyWidget.setWindowTitle(QtGui.QApplication.translate("joyWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.fileLabel.setText(QtGui.QApplication.translate("joyWidget", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.posGroup.setTitle(QtGui.QApplication.translate("joyWidget", "Current Pos", None, QtGui.QApplication.UnicodeUTF8))
        self.BBOxGroup.setTitle(QtGui.QApplication.translate("joyWidget", "Bounding box", None, QtGui.QApplication.UnicodeUTF8))
        self.estTimeGroup.setTitle(QtGui.QApplication.translate("joyWidget", "Estimated time", None, QtGui.QApplication.UnicodeUTF8))
        self.estTimeTxt.setText(QtGui.QApplication.translate("joyWidget", "00:00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("joyWidget", "<html><head/><body><p>Joypad buttons:</p><p>1: Set zero<br/>2: Set Z=0<br/>3: Go to zero</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.RunButton.setText(QtGui.QApplication.translate("joyWidget", "Run (9)", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadButton.setText(QtGui.QApplication.translate("joyWidget", "Load (10)", None, QtGui.QApplication.UnicodeUTF8))

