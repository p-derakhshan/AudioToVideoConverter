from PyQt5 import QtCore, QtGui, QtWidgets
from constants import Constants

C= Constants()

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(C.SC_X,C.SC_Y,C.SC_WIDTH,C.SC_HEIGHT)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-"+C.color_blue_light())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        '''image label'''
        self.lbl_img = QtWidgets.QLabel(self.centralwidget)
        self.lbl_img.setGeometry(QtCore.QRect(20, 30, 281, 401))
        self.lbl_img.setText("")
        self.lbl_img.setPixmap(QtGui.QPixmap("../Images/welcome_transparent.png"))
        self.lbl_img.setObjectName("lbl_img_welcome")
        '''start button'''
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(370, 150, 151, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_start.setFont(font)
        self.btn_start.setStyleSheet("background-"+C.color_blue_dark()+C.color_blue_light())
        self.btn_start.setObjectName("btn_start")
        '''welcome label'''
        self.lbl_welcome = QtWidgets.QLabel(self.centralwidget)
        self.lbl_welcome.setGeometry(QtCore.QRect(20, 45, 281, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_welcome.setFont(font)
        self.lbl_welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_welcome.setObjectName("lbl_welcome")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_start.setText(_translate("MainWindow", "START"))
        self.lbl_welcome.setText(_translate("MainWindow", "Welcome!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
