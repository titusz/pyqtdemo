# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\titusz\Code\pyqtdemo\src/main/python/tutorial/ui\hasher.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetHasher(object):
    def setupUi(self, WidgetHasher):
        WidgetHasher.setObjectName("WidgetHasher")
        WidgetHasher.resize(506, 259)
        self.verticalLayout = QtWidgets.QVBoxLayout(WidgetHasher)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gbox_dropzone = QtWidgets.QGroupBox(WidgetHasher)
        self.gbox_dropzone.setMinimumSize(QtCore.QSize(200, 80))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(9)
        self.gbox_dropzone.setFont(font)
        self.gbox_dropzone.setAcceptDrops(True)
        self.gbox_dropzone.setObjectName("gbox_dropzone")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.gbox_dropzone)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.button_dropzone = QtWidgets.QPushButton(self.gbox_dropzone)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        self.button_dropzone.setFont(font)
        self.button_dropzone.setAcceptDrops(True)
        self.button_dropzone.setStyleSheet("QPushButton:enabled {\n"
"    background-color: #0183ea;\n"
"    color: white;\n"
"}")
        self.button_dropzone.setObjectName("button_dropzone")
        self.verticalLayout_4.addWidget(self.button_dropzone)
        self.verticalLayout.addWidget(self.gbox_dropzone)
        self.gbox_processing_status = QtWidgets.QGroupBox(WidgetHasher)
        self.gbox_processing_status.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(9)
        self.gbox_processing_status.setFont(font)
        self.gbox_processing_status.setObjectName("gbox_processing_status")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gbox_processing_status)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_processing_status = QtWidgets.QLabel(self.gbox_processing_status)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        self.label_processing_status.setFont(font)
        self.label_processing_status.setWordWrap(True)
        self.label_processing_status.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_processing_status.setObjectName("label_processing_status")
        self.verticalLayout_2.addWidget(self.label_processing_status)
        self.progress_bar = QtWidgets.QProgressBar(self.gbox_processing_status)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.progress_bar.setFont(font)
        self.progress_bar.setMaximum(0)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setObjectName("progress_bar")
        self.verticalLayout_2.addWidget(self.progress_bar)
        self.verticalLayout.addWidget(self.gbox_processing_status)
        spacerItem = QtWidgets.QSpacerItem(20, 63, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(WidgetHasher)
        QtCore.QMetaObject.connectSlotsByName(WidgetHasher)

    def retranslateUi(self, WidgetHasher):
        _translate = QtCore.QCoreApplication.translate
        WidgetHasher.setWindowTitle(_translate("WidgetHasher", "Form"))
        self.gbox_dropzone.setTitle(_translate("WidgetHasher", "HASH YOUR FILE"))
        self.button_dropzone.setText(_translate("WidgetHasher", "Drop your file here or click to choose."))
        self.gbox_processing_status.setTitle(_translate("WidgetHasher", "PROCESSING STATUS"))
        self.label_processing_status.setText(_translate("WidgetHasher", "Waiting for file to process"))

