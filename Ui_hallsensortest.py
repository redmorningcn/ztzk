# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\python\pyqt\hallsensortest.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_speedadd = QtWidgets.QPushButton(self.centralwidget)
        self.bt_speedadd.setGeometry(QtCore.QRect(50, 280, 180, 120))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.bt_speedadd.setFont(font)
        self.bt_speedadd.setObjectName("bt_speedadd")
        self.bt_speedsub = QtWidgets.QPushButton(self.centralwidget)
        self.bt_speedsub.setGeometry(QtCore.QRect(300, 280, 180, 120))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.bt_speedsub.setFont(font)
        self.bt_speedsub.setObjectName("bt_speedsub")
        self.bt_shutdown = QtWidgets.QPushButton(self.centralwidget)
        self.bt_shutdown.setGeometry(QtCore.QRect(540, 280, 180, 120))
        self.bt_shutdown.setObjectName("bt_shutdown")
        self.ln_speed = QtWidgets.QLCDNumber(self.centralwidget)
        self.ln_speed.setGeometry(QtCore.QRect(193, 86, 461, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.ln_speed.sizePolicy().hasHeightForWidth())
        self.ln_speed.setSizePolicy(sizePolicy)
        self.ln_speed.setProperty("value", 9000.0)
        self.ln_speed.setObjectName("ln_speed")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 418, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 100, 31, 121))
        font = QtGui.QFont()
        font.setFamily("04b_21")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 60, 700, 16))
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(40, 250, 700, 16))
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NANCHE"))
        self.bt_speedadd.setText(_translate("MainWindow", "速度+"))
        self.bt_speedsub.setText(_translate("MainWindow", "速度-"))
        self.bt_shutdown.setText(_translate("MainWindow", "关机"))
        self.label.setText(_translate("MainWindow", "非接触式霍尔便携测试设备"))
        self.label_2.setText(_translate("MainWindow", "长沙楠车电气设备有限公司  redmorningcn"))
        self.label_3.setText(_translate("MainWindow", "转\n"
"速"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
