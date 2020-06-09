# -*- coding: utf-8 -*-
"""
@Time: 2020.6.9
@Author: Andy.Yang
@File: parsemf4.py
@Software: VS Code

    This app will load a MF4 file, than show the vars using the mdfreader.
"""

import sys

import os.path
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
try:
    import mdfreader
except ImportError:
    print("Pls install mdfreader by 'pip3 install mdfreader' first.")

from form import Ui_Form


class ParseMF4(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(ParseMF4, self).__init__(parent=parent)
        self.setupUi(self)
        self._showVersion()
        self.chs=[]

    @pyqtSlot()
    def on_btn_loadFile_clicked(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "select file", "D:/",
                                                  "MF4(*);;Text Files(*.MF4)",
                                                  "Text Files(*.MF4)")
        fileName = os.path.basename(filePath)
        self.labbel_fileName.setText(fileName)
        self._parseMF4(filePath)
    
    @pyqtSlot()
    def on_btn_save_clicked(self):
        filename = QFileDialog.getSaveFileName(self, 'save file', '', 'Text File(*.txt)')

        with open(filename[0], mode='w', encoding='utf-8') as f:
            savedStdout = sys.stdout
            sys.stdout=f
            for ch in self.chs:
                print(ch)
            sys.stdout=savedStdout

    def _parseMF4(self, pth):
        try:
            mdf=mdfreader.Mdf(pth)
        except:
            print("use mdfreader parse file Error")
        
        for group, channels in mdf.masterChannelList.items():
            for ch in channels:
                self.textBox_show.append(f"{ch}")
                self.chs.append(ch)

    def _showVersion(self):
        self.label_version.setText(
            f"mdfreader version:{mdfreader.__version__}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ParseMF4()
    window.show()
    sys.exit(app.exec_())
