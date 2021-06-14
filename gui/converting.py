from PyQt5 import QtCore, QtGui, QtWidgets
from constants import Constants
import os, time,webbrowser,sys
C= Constants()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self,audio_dir,output_dir,script_dir):
        super(Ui_MainWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.setGeometry(C.SC_X,C.SC_Y,C.SC_WIDTH,C.SC_HEIGHT)
        self.setStyleSheet("background-"+C.color_blue_light())
        self.file_dir = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+ os.sep + os.pardir)
        icon_path = "Images/icon.png"
        file_path = os.path.join(self.file_dir, icon_path)
        self.setWindowIcon(QtGui.QIcon(file_path))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.audio_dir=audio_dir
        self.output_dir=output_dir
        self.script_dir=script_dir
        self.done=False
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
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 400, 75, 23))
        self.pushButton.setStyleSheet("background-"+C.color_blue_dark()+C.color_blue_light())
        self.pushButton.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(self.click)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 200, 151, 31))
        self.pushButton_2.setStyleSheet("background-"+C.color_blue_dark()+C.color_blue_light())
        self.pushButton_2.setObjectName("pushButton_3")
        self.pushButton_2.setHidden(True)
        self.pushButton_2.clicked.connect(self.open_folder)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 400, 75, 23))
        self.pushButton_3.setStyleSheet("background-"+C.color_blue_dark()+C.color_blue_light())
        self.pushButton_3.setObjectName("pushButton_2")
        self.pushButton_3.clicked.connect(self.progressBar_method)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AudioToVideo", "AudioToVideo"))
        self.label.setText(_translate("MainWindow", " "))
        self.pushButton.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_2.setText(_translate("MainWindow", "Open file directory"))
        self.pushButton_3.setText(_translate("MainWindow", "START"))
    def progressBar_method(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "converting..."))
        self.pushButton_3.setHidden(True)
        for i in range(101):
            time.sleep(0.01)
            self.progressBar.setValue(i)
        self.done=True
        self.pushButton_2.setHidden(False)
        self.label.setText(_translate("MainWindow", "Done"))
        self.pushButton.setText(_translate("MainWindow", "Again"))
    def open_folder(self):
        webbrowser.open(self.output_dir)
    def click(self):
        if not self.done:
            self.close()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
