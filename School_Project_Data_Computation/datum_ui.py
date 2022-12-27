# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'INTERFACE2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 795)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(657, 795))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.APP_NAME = QtWidgets.QLabel(self.centralwidget)
        self.APP_NAME.setFrameShape(QtWidgets.QFrame.Box)
        self.APP_NAME.setAlignment(QtCore.Qt.AlignCenter)
        self.APP_NAME.setObjectName("APP_NAME")
        self.horizontalLayout.addWidget(self.APP_NAME)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.WGS_84_NAME = QtWidgets.QLabel(self.centralwidget)
        self.WGS_84_NAME.setFrameShape(QtWidgets.QFrame.Box)
        self.WGS_84_NAME.setAlignment(QtCore.Qt.AlignCenter)
        self.WGS_84_NAME.setObjectName("WGS_84_NAME")
        self.horizontalLayout_4.addWidget(self.WGS_84_NAME)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(16, 220))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setRowCount(1000)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(5)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(5)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.QGIS_UNIT_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.QGIS_UNIT_LABEL.setFrameShape(QtWidgets.QFrame.Box)
        self.QGIS_UNIT_LABEL.setObjectName("QGIS_UNIT_LABEL")
        self.horizontalLayout_10.addWidget(self.QGIS_UNIT_LABEL)
        self.WGS_COMBO_BOX = QtWidgets.QComboBox(self.centralwidget)
        self.WGS_COMBO_BOX.setObjectName("WGS_COMBO_BOX")
        self.WGS_COMBO_BOX.addItem("")
        self.WGS_COMBO_BOX.addItem("")
        self.horizontalLayout_10.addWidget(self.WGS_COMBO_BOX)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.EXPORT_WGS_POINT_TO_EXCEL_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EXPORT_WGS_POINT_TO_EXCEL_BUTTON.sizePolicy().hasHeightForWidth())
        self.EXPORT_WGS_POINT_TO_EXCEL_BUTTON.setSizePolicy(sizePolicy)
        self.EXPORT_WGS_POINT_TO_EXCEL_BUTTON.setObjectName("EXPORT_WGS_POINT_TO_EXCEL_BUTTON")
        self.verticalLayout.addWidget(self.EXPORT_WGS_POINT_TO_EXCEL_BUTTON, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.COORDINATE_CONVERSION_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.COORDINATE_CONVERSION_BUTTON.sizePolicy().hasHeightForWidth())
        self.COORDINATE_CONVERSION_BUTTON.setSizePolicy(sizePolicy)
        self.COORDINATE_CONVERSION_BUTTON.setObjectName("COORDINATE_CONVERSION_BUTTON")
        self.horizontalLayout_6.addWidget(self.COORDINATE_CONVERSION_BUTTON)
        self.COORDINATE_CONVERSION_COMMBO_BOX = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.COORDINATE_CONVERSION_COMMBO_BOX.sizePolicy().hasHeightForWidth())
        self.COORDINATE_CONVERSION_COMMBO_BOX.setSizePolicy(sizePolicy)
        self.COORDINATE_CONVERSION_COMMBO_BOX.setObjectName("COORDINATE_CONVERSION_COMMBO_BOX")
        self.COORDINATE_CONVERSION_COMMBO_BOX.addItem("")
        self.COORDINATE_CONVERSION_COMMBO_BOX.addItem("")
        self.horizontalLayout_6.addWidget(self.COORDINATE_CONVERSION_COMMBO_BOX)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.GHANA_NATIONAL_GRID_NAME = QtWidgets.QLabel(self.centralwidget)
        self.GHANA_NATIONAL_GRID_NAME.setFrameShape(QtWidgets.QFrame.Box)
        self.GHANA_NATIONAL_GRID_NAME.setAlignment(QtCore.Qt.AlignCenter)
        self.GHANA_NATIONAL_GRID_NAME.setObjectName("GHANA_NATIONAL_GRID_NAME")
        self.verticalLayout.addWidget(self.GHANA_NATIONAL_GRID_NAME)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(0, 224))
        self.tableWidget_2.setRowCount(1000)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(5)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(5)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.tableWidget_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.GHANA_NATIONAL_COODINATE_UNIT_LABEL = QtWidgets.QLabel(self.centralwidget)
        self.GHANA_NATIONAL_COODINATE_UNIT_LABEL.setFrameShape(QtWidgets.QFrame.Box)
        self.GHANA_NATIONAL_COODINATE_UNIT_LABEL.setObjectName("GHANA_NATIONAL_COODINATE_UNIT_LABEL")
        self.horizontalLayout_3.addWidget(self.GHANA_NATIONAL_COODINATE_UNIT_LABEL)
        self.GHANA_NATIONAL_UNIT_COMBOBOX = QtWidgets.QComboBox(self.centralwidget)
        self.GHANA_NATIONAL_UNIT_COMBOBOX.setObjectName("GHANA_NATIONAL_UNIT_COMBOBOX")
        self.GHANA_NATIONAL_UNIT_COMBOBOX.addItem("")
        self.GHANA_NATIONAL_UNIT_COMBOBOX.addItem("")
        self.horizontalLayout_3.addWidget(self.GHANA_NATIONAL_UNIT_COMBOBOX)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter)
        self.GHANA_NATIONAL_POINT_EXPORT_TO_EXCEL_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GHANA_NATIONAL_POINT_EXPORT_TO_EXCEL_BUTTON.sizePolicy().hasHeightForWidth())
        self.GHANA_NATIONAL_POINT_EXPORT_TO_EXCEL_BUTTON.setSizePolicy(sizePolicy)
        self.GHANA_NATIONAL_POINT_EXPORT_TO_EXCEL_BUTTON.setObjectName("GHANA_NATIONAL_POINT_EXPORT_TO_EXCEL_BUTTON")
        self.verticalLayout.addWidget(self.GHANA_NATIONAL_POINT_EXPORT_TO_EXCEL_BUTTON, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.APP_NAME.setText(_translate("MainWindow", "2D CONFORMAL DATUM TRANSFORMATION"))
        self.WGS_84_NAME.setText(_translate("MainWindow", "WGS 84 GEOGRAPHICAL CORDINATE"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "LAT"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "LONG"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CORESS. N"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CORESS.E"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "LAT FOR EXPECTED GRID"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "LON FOR EXPECTED GRID"))
        self.QGIS_UNIT_LABEL.setText(_translate("MainWindow", "UNIT"))
        self.WGS_COMBO_BOX.setItemText(0, _translate("MainWindow", "UTM_METERS"))
        self.WGS_COMBO_BOX.setItemText(1, _translate("MainWindow", "UTM_FEETS"))
        self.pushButton.setText(_translate("MainWindow", "CLEAR TABLE"))
        self.EXPORT_WGS_POINT_TO_EXCEL_BUTTON.setText(_translate("MainWindow", "EXPORT TO EXCEL"))
        self.COORDINATE_CONVERSION_BUTTON.setText(_translate("MainWindow", "CONVERT TO"))
        self.COORDINATE_CONVERSION_COMMBO_BOX.setItemText(0, _translate("MainWindow", "WGS 84"))
        self.COORDINATE_CONVERSION_COMMBO_BOX.setItemText(1, _translate("MainWindow", "GHANA NATIONAL  GRID"))
        self.GHANA_NATIONAL_GRID_NAME.setText(_translate("MainWindow", "GHANA NATIONAL GRID"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "N"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "E"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CORESS.LAT"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CORRES. LONG"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "EXPECTED  N FOR UTM"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "EXPECTED E FOR UTM"))
        self.GHANA_NATIONAL_COODINATE_UNIT_LABEL.setText(_translate("MainWindow", "UNIT"))
        self.GHANA_NATIONAL_UNIT_COMBOBOX.setItemText(0, _translate("MainWindow", "GRID_FEETS"))
        self.GHANA_NATIONAL_UNIT_COMBOBOX.setItemText(1, _translate("MainWindow", "GRID_METERS"))
        self.pushButton_2.setText(_translate("MainWindow", "CLEAR TABLE"))
        self.GHANA_NATIONAL_POINT_EXPORT_TO_EXCEL_BUTTON.setText(_translate("MainWindow", "EXPORT TO EXCEL"))