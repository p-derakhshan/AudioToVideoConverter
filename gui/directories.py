from PyQt5 import QtCore, QtGui, QtWidgets
from constants import Constants
import sys, converting, os

C= Constants()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.setGeometry(C.SC_X,C.SC_Y,C.SC_WIDTH,C.SC_HEIGHT)
        self.setStyleSheet("background-"+C.color_blue_light())
        self.file_dir = os.path.normpath(os.path.dirname(os.path.realpath(__file__))+ os.sep + os.pardir)
        icon_path = "Images/icon.png"
        file_path = os.path.join(self.file_dir, icon_path)
        self.setWindowIcon(QtGui.QIcon(file_path))
        self.centralwidget = QtWidgets.QWidget(self)
        self.audio_dir=''
        self.output_dir=''
        self.script_dir=''
        self.centralwidget.setObjectName("centralwidget")
        self.setupUi()

    def setupUi(self):
        self.lbl_audio_dir = QtWidgets.QLabel(self.centralwidget)
        self.lbl_audio_dir.setGeometry(QtCore.QRect(10, 20, 571, 16))
        self.lbl_audio_dir.setObjectName("lbl_audio_dir")
        self.txt_output_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_output_dir.setGeometry(QtCore.QRect(10, 110, 571, 25))
        self.txt_output_dir.setStyleSheet("background-"+C.color_white())
        self.txt_output_dir.setText("")
        self.txt_audio_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_audio_dir.setGeometry(QtCore.QRect(10, 50, 571, 25))
        self.txt_audio_dir.setStyleSheet("background-"+C.color_white())
        self.txt_audio_dir.setText("")
        self.lbl_out_dir = QtWidgets.QLabel(self.centralwidget)
        self.lbl_out_dir.setGeometry(QtCore.QRect(10, 90, 571, 16))
        self.lbl_out_dir.setObjectName("lbl_out_dir")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 150, 571, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(self.check_b)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 180, 571, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(self.check_b2)
        self.lbl_script_dir = QtWidgets.QLabel(self.centralwidget)
        self.lbl_script_dir.setGeometry(QtCore.QRect(10, 210, 571, 16))
        self.lbl_script_dir.setObjectName("lbl_script_dir")
        self.lbl_script_dir.setHidden(True)
        self.txt_script_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_script_dir.setGeometry(QtCore.QRect(10, 240, 571, 25))
        self.txt_script_dir.setStyleSheet("background-"+C.color_white())
        self.txt_script_dir.setText("")
        self.txt_script_dir.setObjectName("txt_script_dir")
        self.txt_script_dir.setHidden(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 400, 75, 23))
        self.pushButton.setStyleSheet("background-"+C.color_blue_dark()+C.color_blue_light())
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 400, 75, 23))
        self.pushButton_2.setStyleSheet("background-"+C.color_blue_dark()+C.color_blue_light())
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.click_run)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AudioToVideo", "AudioToVideo"))
        self.lbl_audio_dir.setText(_translate("MainWindow", "Choose Audio File Directory:"))
        self.lbl_out_dir.setText(_translate("MainWindow", "Choose Output Directory:"))
        self.checkBox.setText(_translate("MainWindow", "I just want the text file"))
        self.checkBox_2.setText(_translate("MainWindow", "I have the script"))
        self.lbl_script_dir.setText(_translate("MainWindow", "Choose Text File Directory:"))
        self.pushButton.setText(_translate("MainWindow", "CANCEL"))
        self.pushButton_2.setText(_translate("MainWindow", "RUN"))
    def check_b(self):
        if self.checkBox.isChecked():
            self.checkBox_2.setCheckable(False)
            self.checkBox_2.setStyleSheet("QCheckBox::indicator{ border: 1px solid black; background-"+C.color_gray_light()+
"}\n"
"")
        else:
            self.checkBox_2.setCheckable(True)
            self.checkBox_2.setStyleSheet("")
        
    def check_b2(self):
        if self.checkBox_2.isChecked():
            self.checkBox.setCheckable(False)
            self.checkBox.setStyleSheet("QCheckBox::indicator{ border: 1px solid black; background-"+C.color_gray_light()+
"}\n"
"")
            self.lbl_script_dir.setHidden(False)
            self.txt_script_dir.setHidden(False)
        else:
            self.lbl_script_dir.setHidden(True)
            self.txt_script_dir.setHidden(True)
            self.checkBox.setCheckable(True)
            self.checkBox.setStyleSheet("")

    def click_run(self):
        self.audio_dir = self.txt_audio_dir.text()
        self.output_dir = self.txt_output_dir.text()
        self.script_dir = self.txt_script_dir.text() 
        self.ui_convert = converting.Ui_MainWindow(self.audio_dir,self.output_dir, self.script_dir)
        self.ui_convert.show()
        self.close()
