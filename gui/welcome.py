from PyQt5 import QtCore, QtGui, QtWidgets
from constants import Constants
import sys , directories, os

C= Constants()

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.setGeometry(C.SC_X,C.SC_Y,C.SC_WIDTH,C.SC_HEIGHT)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-"+C.color_blue_light())
        self.script_dir = os.path.dirname(__file__) 
        icon_path = "../images/icon.png"
        file_path = os.path.join(self.script_dir, icon_path)
        self.setWindowIcon(QtGui.QIcon(file_path ))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.ui_dir = directories.Ui_MainWindow()
        self.setupUi()
        

    def setupUi(self):
        '''image label'''
        self.lbl_img = QtWidgets.QLabel(self.centralwidget)
        self.lbl_img.setGeometry(QtCore.QRect(20, 70, 281, 401))
        self.lbl_img.setText("") 
        rel_path = "../images/welcome_transparent.png"
        abs_file_path = os.path.join(self.script_dir, rel_path)
        pixmap = QtGui.QPixmap(abs_file_path)
        self.lbl_img.setPixmap(pixmap)
        self.lbl_img.setObjectName("lbl_img_welcome")
        self.lbl_img.resize(pixmap.width(),pixmap.height())
        '''start button'''
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(370, 150, 151, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_start.setFont(font)
        self.btn_start.setStyleSheet("background-"+C.color_blue_dark()+C.color_blue_light())
        self.btn_start.setObjectName("btn_start")
        self.btn_start.clicked.connect(self.click_start)
        '''welcome label'''
        self.lbl_welcome = QtWidgets.QLabel(self.centralwidget)
        self.lbl_welcome.setGeometry(QtCore.QRect(25, 35, 281, 25))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_welcome.setFont(font)
        self.lbl_welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_welcome.setObjectName("lbl_welcome")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("AudioToVideo", "AudioToVideo"))
        self.btn_start.setText(_translate("MainWindow", "START"))
        self.lbl_welcome.setText(_translate("MainWindow", "Welcome!"))

    def click_start(self):
        self.ui_dir.show()
        self.close()


if __name__ == "__main__":
    pass
app = QtWidgets.QApplication(sys.argv)
ui = Ui_MainWindow()
ui.show()
app.exec()