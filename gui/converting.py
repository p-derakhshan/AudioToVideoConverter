from PyQt5 import QtCore, QtGui, QtWidgets
from constants import Constants
import os

C= Constants()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.setGeometry(C.SC_X,C.SC_Y,C.SC_WIDTH,C.SC_HEIGHT)
        self.setStyleSheet("background-"+C.color_blue_light())
        script_dir = os.path.dirname(__file__) 
        rel_path = "../images/icon.png"
        abs_file_path = os.path.join(script_dir, rel_path)
        self.setWindowIcon(QtGui.QIcon(abs_file_path ))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setupUi()

    def setupUi(self):
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 110, 531, 31))
        self.progressBar.setStyleSheet("QProgressBar::chunk { background-"+C.color_blue_dark()+
"}\n"
"")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(440, 400, 75, 23))
        self.pushButton.setStyleSheet("background-"+C.color_blue_dark()+C.color_blue_light())
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 400, 75, 23))
        self.pushButton_2.setStyleSheet("background-"+C.color_blue_dark()+C.color_blue_light())
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 200, 151, 31))
        self.pushButton_3.setStyleSheet("background-"+C.color_blue_dark()+C.color_blue_light())
        self.pushButton_3.setObjectName("pushButton_3")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AudioToVideo", "AudioToVideo"))
        self.label.setText(_translate("MainWindow", "converting"))
        self.pushButton.setText(_translate("MainWindow", "Again"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_3.setText(_translate("MainWindow", "Open file directory"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
