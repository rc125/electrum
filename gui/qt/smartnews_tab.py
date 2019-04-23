import os
import traceback

from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor
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
        self.windows = []
        self.webView = HtmlView(self.windows)
        self.webView.load(self.url)

        self.verticalLayout.addWidget(self.webView)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

class WebEnginePage(QWebEnginePage):
    def acceptNavigationRequest(self, url,  _type, isMainFrame):
        if _type == QWebEnginePage.NavigationTypeLinkClicked:
            return True
        return super(WebEnginePage, self).acceptNavigationRequest(url, _type, isMainFrame)

class HtmlView(QWebEngineView):
    def __init__(self, windows, *args, **kwargs):
        super(HtmlView, self).__init__(*args, **kwargs)
        self.setPage(WebEnginePage(self))
        self._windows = windows
        self._windows.append(self)

    def createWindow(self, _type):
        if QWebEnginePage.WebBrowserTab:
            v = HtmlView(self._windows)
            v.resize(640, 480)
            v.show()
            return v