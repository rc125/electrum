
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SmartNewsWidget(object):
    def setupUi(self, SmartProposalWidget):
        SmartProposalWidget.setObjectName("SmartProposalWidget")
        SmartProposalWidget.resize(865, 232)
        SmartProposalWidget.setStyleSheet('#SmartProposalWidget{\n'
                                          'border: 1px solid black;\n'
                                          'border-radius: 5px;\n'
                                          'background-color: #FBFCFC;\n'
                                          '}')
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(SmartProposalWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.titleLabel = QtWidgets.QLabel(SmartProposalWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.titleLabel.setWordWrap(True)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout_4.addWidget(self.titleLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(SmartProposalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.label.setWordWrap(True);
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.viewProposalButton = QtWidgets.QPushButton(SmartProposalWidget)
        self.viewProposalButton.setAutoDefault(False)
        self.viewProposalButton.setFlat(False)
        self.viewProposalButton.setObjectName("viewProposalButton")
        self.horizontalLayout_2.addWidget(self.viewProposalButton)
        spacerItem = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        #spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        #self.horizontalLayout_3.addItem(spacerItem1)

        self.retranslateUi(SmartProposalWidget)
        QtCore.QMetaObject.connectSlotsByName(SmartProposalWidget)

    def retranslateUi(self, SmartProposalWidget):
        _translate = QtCore.QCoreApplication.translate
        SmartProposalWidget.setWindowTitle(_translate("SmartProposalWidget", "Form"))
        self.titleLabel.setText(_translate("SmartProposalWidget", "SmartCash Tip Bot Makes it Easy to Tip Anyone"))
        self.groupBox_2.setTitle(_translate("SmartProposalWidget", "April 12, 2019 - coinlance.com"))
        self.label.setText(_translate("SmartProposalWidget", "A cryptocurrency themed Augmented Reality game called Crypto Hunters has been released for beta and SmartCash is on the list of currencies involved with the project! Created by SWYFT with the intent of helping to..."))
        self.viewProposalButton.setText(_translate("SmartProposalWidget", "Read more"))

