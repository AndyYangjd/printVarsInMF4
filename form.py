# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(525, 395)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hbox_load = QtWidgets.QHBoxLayout()
        self.hbox_load.setObjectName("hbox_load")
        self.btn_loadFile = QtWidgets.QPushButton(Form)
        self.btn_loadFile.setObjectName("btn_loadFile")
        self.hbox_load.addWidget(self.btn_loadFile)
        self.labbel_fileName = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labbel_fileName.setFont(font)
        self.labbel_fileName.setObjectName("labbel_fileName")
        self.hbox_load.addWidget(self.labbel_fileName)
        self.hbox_load.setStretch(0, 1)
        self.hbox_load.setStretch(1, 4)
        self.verticalLayout.addLayout(self.hbox_load)
        self.textBox_show = QtWidgets.QTextBrowser(Form)
        self.textBox_show.setObjectName("textBox_show")
        self.verticalLayout.addWidget(self.textBox_show)
        self.hbox_save = QtWidgets.QHBoxLayout()
        self.hbox_save.setObjectName("hbox_save")
        self.btn_save = QtWidgets.QPushButton(Form)
        self.btn_save.setObjectName("btn_save")
        self.hbox_save.addWidget(self.btn_save)
        self.label_version = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_version.setFont(font)
        self.label_version.setObjectName("label_version")
        self.hbox_save.addWidget(self.label_version)
        self.hbox_save.setStretch(0, 1)
        self.hbox_save.setStretch(1, 4)
        self.verticalLayout.addLayout(self.hbox_save)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "show Vars in MF4"))
        self.btn_loadFile.setText(_translate("Form", "LoadFile"))
        self.labbel_fileName.setText(_translate("Form", "MF4 file name"))
        self.btn_save.setText(_translate("Form", "Save"))
        self.label_version.setText(_translate("Form", "mdfreader version:"))
