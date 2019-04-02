import os
import traceback

from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from . import util

class SmartnewsTab(QWidget):

    def __init__(self, parent=None):
        super(SmartnewsTab, self).__init__(parent)
        self.gui = parent
        self.create_layout()

    def create_layout(self):
        self.setObjectName("Form")
        self.resize(794, 441)
        self.webView = QWebEngineView(self)
        self.webView.setGeometry(QRect(0, 0, 791, 421))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setUrl(QUrl("file:///home/renatocruz/Desktop/smartnews.html"))
        self.webView.setObjectName("webView")

        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, SmartVotingPage):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))