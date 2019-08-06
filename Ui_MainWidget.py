# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/MainWidget.ui',
# licensing of 'res/MainWidget.ui' applies.
#
# Created: Tue Aug  6 15:36:54 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.resize(1010, 401)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWidget.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MainWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.widgetInputDraw = DrawInput(self.groupBox)
        self.widgetInputDraw.setProperty("CellSize", QtCore.QSize(10, 10))
        self.widgetInputDraw.setProperty("CellCount", QtCore.QSize(10, 10))
        self.widgetInputDraw.setObjectName("widgetInputDraw")
        self.horizontalLayout_3.addWidget(self.widgetInputDraw)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBoxInteractive = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxInteractive.setObjectName("checkBoxInteractive")
        self.horizontalLayout_2.addWidget(self.checkBoxInteractive)
        self.pushButtonPredict = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonPredict.setObjectName("pushButtonPredict")
        self.horizontalLayout_2.addWidget(self.pushButtonPredict)
        self.pushButtonClear = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout_2.addWidget(self.pushButtonClear)
        self.pushButtonSelectFromDataSet = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonSelectFromDataSet.setObjectName("pushButtonSelectFromDataSet")
        self.horizontalLayout_2.addWidget(self.pushButtonSelectFromDataSet)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 12)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(MainWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/brain.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.comboBoxModel = QtWidgets.QComboBox(MainWidget)
        self.comboBoxModel.setObjectName("comboBoxModel")
        self.verticalLayout_2.addWidget(self.comboBoxModel)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(MainWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widgetHistogram = HistogramWidget(self.groupBox_2)
        self.widgetHistogram.setObjectName("widgetHistogram")
        self.verticalLayout_3.addWidget(self.widgetHistogram)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout.setStretch(0, 7)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 7)

        self.retranslateUi(MainWidget)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QtWidgets.QApplication.translate("MainWidget", "MNIST Digit Recognition Visualizer", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWidget", "Input", None, -1))
        self.checkBoxInteractive.setText(QtWidgets.QApplication.translate("MainWidget", "Interactive", None, -1))
        self.pushButtonPredict.setText(QtWidgets.QApplication.translate("MainWidget", "Predict", None, -1))
        self.pushButtonClear.setText(QtWidgets.QApplication.translate("MainWidget", "Clear", None, -1))
        self.pushButtonSelectFromDataSet.setText(QtWidgets.QApplication.translate("MainWidget", "Test image", None, -1))
        self.comboBoxModel.setToolTip(QtWidgets.QApplication.translate("MainWidget", "Select model", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWidget", "Output", None, -1))

from DrawInput import DrawInput
from HistogramWidget import HistogramWidget
import resources_rc
