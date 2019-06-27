import os
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets
from .smartnews_list import Ui_SmartNewsWidget
import requests
from electrum_smart.util import print_msg


class SmartnewsTab(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(SmartnewsTab, self).__init__(parent)
        self.gui = parent
        self.setupUi(self)
        self.on_load_news_successful()

    def setupUi(self, SmartNewsPage):
        SmartNewsPage.setObjectName("SmartNewsPage")
        SmartNewsPage.resize(811, 457)
        SmartNewsPage.setStyleSheet('#newsList{\n'
                                          'background-color: #FCFCFC;\n'
                                          '}'
                                    '#scrollArea{\n'
                                    'border: none;\n'
                                    '}'
                                    )
        self.verticalLayout = QtWidgets.QVBoxLayout(SmartNewsPage)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(SmartNewsPage)
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget.addWidget(self.page)
        self.loadingPage = QtWidgets.QWidget()
        self.loadingPage.setObjectName("loadingPage")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.loadingPage)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.stackedWidget.addWidget(self.loadingPage)
        self.newsPage = QtWidgets.QWidget()
        self.newsPage.setMinimumSize(QtCore.QSize(0, 0))
        self.newsPage.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.newsPage.setObjectName("newsPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.newsPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.newsPage)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.newsList = QtWidgets.QWidget()
        self.newsList.setGeometry(QtCore.QRect(0, 0, 787, 394))
        self.newsList.setObjectName("newsList")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.newsList)
        self.verticalLayout_6.setContentsMargins(9, -1, 9, -1)
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea.setWidget(self.newsList)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        #self.refreshButton = QtWidgets.QPushButton(self.newsPage)
        #self.refreshButton.setObjectName("refreshButton")
        #self.horizontalLayout_2.addWidget(self.refreshButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.newsPage)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(SmartNewsPage)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(SmartNewsPage)

    def retranslateUi(self, SmartNewsPage):
        _translate = QtCore.QCoreApplication.translate
        SmartNewsPage.setWindowTitle(_translate("SmartNewsPage", "Form"))
        #self.refreshButton.setText(_translate("SmartNewsPage", "Refresh List"))

    def on_load_news_successful(self):

        print_msg('Loading news')
        json = self.get_json('smartnews.claus235.dev', '/smartnews.json')

        if json:
            news_qtd = 0
            for item in json['itens']:
                try:
                    SmartnewsListWidget = QtWidgets.QWidget()
                    ui = Ui_SmartNewsWidget()
                    ui.setupUi(SmartnewsListWidget, item)
                    self.verticalLayout_6.addWidget(SmartnewsListWidget)
                    news_qtd += 1
                    if news_qtd == 5:
                        break
                except Exception as e:
                    print_msg("could not load news: {}".format(str(e)))
                    return
        else:
            print_msg('Could not load news api')

    def get_json(self, site, get_string):
        # APIs must have https
        url = ''.join(['https://', site, get_string])
        response = requests.request('GET', url, headers={'User-Agent' : 'Electrum'}, timeout=10)
        return response.json()
