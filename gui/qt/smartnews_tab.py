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

        self.setObjectName("News")
        self.setEnabled(True)
        self.resize(832, 629)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.webView = QWebEngineView(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setUrl(QUrl("https://electrum-news.rc125.cc/"))
        self.webView.setObjectName("webView")

        self.verticalLayout.addWidget(self.webView)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
