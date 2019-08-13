# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Config.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtCore.QCoreApplication.translate(context, text, disambig)

class Ui_dlg_config(object):
    def setupUi(self, dlg_config):
        dlg_config.setObjectName("dlg_config")
        dlg_config.resize(395, 473)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":icon/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlg_config.setWindowIcon(icon)
        self.gridLayout_6 = QtWidgets.QGridLayout(dlg_config)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(dlg_config)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(dlg_config)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.check_overall = QtWidgets.QCheckBox(self.groupBox)
        self.check_overall.setObjectName("check_overall")
        self.horizontalLayout_2.addWidget(self.check_overall)
        self.check_deck = QtWidgets.QCheckBox(self.groupBox)
        self.check_deck.setObjectName("check_deck")
        self.horizontalLayout_2.addWidget(self.check_deck)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.groupBox_3 = QtWidgets.QGroupBox(dlg_config)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.check_start = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_start.setObjectName("check_start")
        self.verticalLayout.addWidget(self.check_start)
        self.check_break = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_break.setObjectName("check_break")
        self.verticalLayout.addWidget(self.check_break)
        self.check_almost_timeout = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_almost_timeout.setObjectName("check_almost_timeout")
        self.verticalLayout.addWidget(self.check_almost_timeout)
        self.check_timeout = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_timeout.setObjectName("check_timeout")
        self.verticalLayout.addWidget(self.check_timeout)
        self.check_abort = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_abort.setObjectName("check_abort")
        self.verticalLayout.addWidget(self.check_abort)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.gridLayout_6.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(dlg_config)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(6, 1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout_4.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.tableWidget.raise_()
        self.label_2.raise_()
        self.gridLayout_6.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.retranslateUi(dlg_config)
        QtCore.QMetaObject.connectSlotsByName(dlg_config)

    def retranslateUi(self, dlg_config):
        dlg_config.setWindowTitle(_translate("dlg_config", "Config", None))
        self.groupBox_2.setTitle(_translate("dlg_config", "Timeout", None))
        self.groupBox.setTitle(_translate("dlg_config", "Show Statistics", None))
        self.check_overall.setText(_translate("dlg_config", "Overall", None))
        self.check_deck.setText(_translate("dlg_config", "Deck", None))
        self.groupBox_3.setTitle(_translate("dlg_config", "Play Sounds", None))
        self.check_start.setText(_translate("dlg_config", "Start", None))
        self.check_break.setText(_translate("dlg_config", "Break", None))
        self.check_almost_timeout.setText(_translate("dlg_config", "Almost Timeout", None))
        self.check_timeout.setText(_translate("dlg_config", "Timeout", None))
        self.check_abort.setText(_translate("dlg_config", "Abort", None))
        self.groupBox_4.setTitle(_translate("dlg_config", "Tomato Minutes", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("dlg_config", "新建行", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("dlg_config", "新建行", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("dlg_config", "新建行", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("dlg_config", "新建行", None))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("dlg_config", "新建行", None))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("dlg_config", "新建行", None))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("dlg_config", "新建行", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("dlg_config", "Work", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("dlg_config", "Break", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("dlg_config", "Append new Work - Break minutes at the last or Change", None))

from . import resource_rc