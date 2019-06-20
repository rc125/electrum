import os
import traceback

from PyQt5.QtGui import *
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

        self.url = QUrl("https://electrum-news.rc125.cc/")
        self.webView = QWebEngineView()
        self.page = WebEnginePage(self.webView)
        self.webView.setPage(self.page)
        self.webView.load(self.url)

        self.verticalLayout.addWidget(self.webView)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

class WebEnginePage(QWebEnginePage):
    def createWindow(self, _type):
        page = WebEnginePage(self)
        page.urlChanged.connect(self.open_browser)
        return page

    def open_browser(self, url):
        page = self.sender()
        QDesktopServices.openUrl(url)
        page.deleteLater()
