from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
   
    baseState = "Red"
    buttons = ["Button1", "Button2", "Button3", "Button4", "Button5", "Button6", "Button7", "Button8", "Button9"]
    playerState = {}
    score = {}
   
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Tic Tac Toe")
        MainWindow.resize(780, 580)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Score Blue player
        # self.ScoreBlue = QtWidgets.QLabel(self.centralwidget)
        # self.ScoreBlue.setGeometry(QtCore.QRect(180, 5, 200, 80))
        # self.ScoreBlue.setText("0")
        self.ScoreBlue = QtWidgets.QTextBrowser(self.centralwidget)
        self.ScoreBlue.setGeometry(QtCore.QRect(180, 5, 200, 80))
        self.ScoreBlue.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ScoreBlue.setObjectName("ScoreBlue")
        
        #Score Red player
        self.ScoreRed = QtWidgets.QTextBrowser(self.centralwidget)
        self.ScoreRed.setGeometry(QtCore.QRect(400, 5, 200, 80))
        self.ScoreRed.setAutoFillBackground(False)
        self.ScoreRed.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ScoreRed.setObjectName("ScoreRed")
        
        # Map
        self.Map = QtWidgets.QLabel(self.centralwidget)
        self.Map.setGeometry(QtCore.QRect(180, 90, 420, 420))
        self.Map.setObjectName("Map")
        self.Map.setStyleSheet("background-image: url(img/map.png)")

        # Buttons
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(180, 90, 137, 137))
        self.Button1.setObjectName("Button1")
        self.Button1.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Button1.setCheckable(True)
        
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(325, 90, 133, 137))
        self.Button2.setObjectName("Button2")
        self.Button2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Button2.setCheckable(True)
        
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(466, 90, 134, 137))
        self.Button3.setObjectName("Button3")
        self.Button3.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Button3.setCheckable(True)
        
        self.Button4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button4.setGeometry(QtCore.QRect(180, 235, 137, 133))
        self.Button4.setObjectName("Button4")
        self.Button4.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Button4.setCheckable(True)

        self.Button5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button5.setGeometry(QtCore.QRect(325, 235, 133, 134))
        self.Button5.setObjectName("Button5")
        self.Button5.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Button5.setCheckable(True)

        self.Button6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button6.setGeometry(QtCore.QRect(466, 235, 134, 134))
        self.Button6.setObjectName("Button6")
        self.Button6.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Button6.setCheckable(True)

        self.Button7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button7.setGeometry(QtCore.QRect(180, 376, 137, 134))
        self.Button7.setObjectName("Button7")
        self.Button7.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Button7.setCheckable(True)

        self.Button8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button8.setGeometry(QtCore.QRect(325, 376, 133, 134))
        self.Button8.setObjectName("Button8")
        self.Button8.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Button8.setCheckable(True)

        self.Button9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button9.setGeometry(QtCore.QRect(466, 376, 134, 134))
        self.Button9.setObjectName("Button9")
        self.Button9.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Button9.setCheckable(True)

        # Menubar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 26))
        self.menubar.setObjectName("menubar")
        
        self.menuRestart = QtWidgets.QMenu(self.menubar)
        self.menuRestart.setObjectName("menuRestart")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        # Restart option
        MainWindow.setStatusBar(self.statusbar)
        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.menuRestart.addAction(self.actionRestart)
        self.menubar.addAction(self.menuRestart.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.initButtonLog()
        self.initScore()
        self.showPlayer()
        self.updateButtonLog()
        self.updateScore()

    def initButtonLog(self):
        for button in self.buttons:
            self.playerState[button] = ""
        print(self.playerState)

    def initScore(self):
        self.score['Blue'] = 0
        self.score['Red']  = 0
        # self.ScoreBlue.setText(str(self.score["Blue"]))
        # self.ScoreRed.setMarkdown(str(self.score["Red"]))


        # Setup is done
#     def updateUI(self, MainWindow):
#         self.showPlayer(self)
#         self.updateButtonLog()
#         self.updateScore()

    def showPlayer(self):
        if self.baseState == "Red":
            self.Button1.clicked.connect(self.addRedPlayer)
            self.Button2.clicked.connect(self.addRedPlayer)
            self.Button3.clicked.connect(self.addRedPlayer)
            self.Button4.clicked.connect(self.addRedPlayer)
            self.Button5.clicked.connect(self.addRedPlayer)
            self.Button6.clicked.connect(self.addRedPlayer)
            self.Button7.clicked.connect(self.addRedPlayer)
            self.Button8.clicked.connect(self.addRedPlayer)
            self.Button9.clicked.connect(self.addRedPlayer)
        
        elif self.baseState == "Blue":
            self.Button1.clicked.connect(self.addBluePlayer)
            self.Button2.clicked.connect(self.addBluePlayer)
            self.Button3.clicked.connect(self.addBluePlayer)
            self.Button4.clicked.connect(self.addBluePlayer)
            self.Button5.clicked.connect(self.addBluePlayer)
            self.Button6.clicked.connect(self.addBluePlayer)
            self.Button7.clicked.connect(self.addBluePlayer)
            self.Button8.clicked.connect(self.addBluePlayer)
            self.Button9.clicked.connect(self.addBluePlayer)
            self.baseState = "Red"

    def addRedPlayer(self):
        if   self.Button1.isChecked() & (self.baseState == "Red") & (self.playerState["Button1"] == ""):
            self.playerState["Button1"] = self.baseState
            self.baseState = "Blue"
            print("B1")
            print(self.playerState)

            self.Button1.setIcon(QtGui.QIcon("img/redPlayer.png"))
            self.Button1.setIconSize(QtCore.QSize(140,140))
            self.Button1.toggle()
            # self.Button1.setCheckable(False)
        
        elif self.Button1.isChecked() & (self.baseState == "Blue") & (self.playerState["Button1"] == ""):
            self.playerState["Button1"] = self.baseState
            self.baseState = "Red"
            print("B1")
            print(self.playerState)

            self.Button1.setIcon(QtGui.QIcon("img/bluePlayer.png"))
            self.Button1.setIconSize(QtCore.QSize(140,140))
            self.Button1.toggle()
        
        elif self.Button2.isChecked() & (self.baseState == "Red") & (self.playerState["Button2"] == ""):
            self.playerState["Button2"] = self.baseState
            self.baseState = "Blue"
            print("B2")
            print(self.playerState)

            self.Button2.setIcon(QtGui.QIcon("img/redPlayer.png"))
            self.Button2.setIconSize(QtCore.QSize(140,140))
            self.Button2.toggle()
            # self.Button1.setCheckable(False)
        
        elif self.Button2.isChecked() & (self.baseState == "Blue") & (self.playerState["Button2"] == ""):
            self.playerState["Button2"] = self.baseState
            self.baseState = "Red"
            print("B2")
            print(self.playerState)

            self.Button2.setIcon(QtGui.QIcon("img/bluePlayer.png"))
            self.Button2.setIconSize(QtCore.QSize(140,140))
            self.Button2.toggle()

        elif self.Button3.isChecked() & (self.baseState == "Red") & (self.playerState["Button3"] == ""):
            self.playerState["Button3"] = self.baseState
            self.baseState = "Blue"
            print("B3")
            print(self.playerState)

            self.Button3.setIcon(QtGui.QIcon("img/redPlayer.png"))
            self.Button3.setIconSize(QtCore.QSize(140,140))
            self.Button3.toggle()
        
        elif self.Button3.isChecked() & (self.baseState == "Blue") & (self.playerState["Button3"] == ""):
            self.playerState["Button3"] = self.baseState
            self.baseState = "Red"
            print("B3")
            print(self.playerState)

            self.Button3.setIcon(QtGui.QIcon("img/bluePlayer.png"))
            self.Button3.setIconSize(QtCore.QSize(140,140))
            self.Button3.toggle()

        elif self.Button4.isChecked() & (self.baseState == "Red") & (self.playerState["Button4"] == ""):
            self.playerState["Button4"] = self.baseState
            self.baseState = "Blue"
            print("B4")
            print(self.playerState)

            self.Button4.setIcon(QtGui.QIcon("img/redPlayer.png"))
            self.Button4.setIconSize(QtCore.QSize(140,140))
            self.Button4.toggle()
        
        elif self.Button4.isChecked() & (self.baseState == "Blue") & (self.playerState["Button4"] == ""):
            self.playerState["Button4"] = self.baseState
            self.baseState = "Red"
            print("B4")
            print(self.playerState)

            self.Button4.setIcon(QtGui.QIcon("img/bluePlayer.png"))
            self.Button4.setIconSize(QtCore.QSize(140,140))
            self.Button4.toggle()
        
        elif self.Button5.isChecked() & (self.baseState == "Red") & (self.playerState["Button5"] == ""):
            self.playerState["Button5"] = self.baseState
            self.baseState = "Blue"
            print("B5")
            print(self.playerState)

            self.Button5.setIcon(QtGui.QIcon("img/redPlayer.png"))
            self.Button5.setIconSize(QtCore.QSize(140,140))
            self.Button5.toggle()
        
        elif self.Button5.isChecked() & (self.baseState == "Blue") & (self.playerState["Button5"] == ""):
            self.playerState["Button5"] = self.baseState
            self.baseState = "Red"
            print("B5")
            print(self.playerState)

            self.Button5.setIcon(QtGui.QIcon("img/bluePlayer.png"))
            self.Button5.setIconSize(QtCore.QSize(140,140))
            self.Button5.toggle()

        elif self.Button6.isChecked() & (self.baseState == "Red") & (self.playerState["Button6"] == ""):
            self.playerState["Button6"] = self.baseState
            self.baseState = "Blue"
            print("B6")
            print(self.playerState)

            self.Button6.setIcon(QtGui.QIcon("img/redPlayer.png"))
            self.Button6.setIconSize(QtCore.QSize(140,140))
            self.Button6.toggle()
        
        elif self.Button6.isChecked() & (self.baseState == "Blue") & (self.playerState["Button6"] == ""):
            self.playerState["Button6"] = self.baseState
            self.baseState = "Red"
            print("B6")
            print(self.playerState)

            self.Button6.setIcon(QtGui.QIcon("img/bluePlayer.png"))
            self.Button6.setIconSize(QtCore.QSize(140,140))
            self.Button6.toggle()

        elif self.Button7.isChecked() & (self.baseState == "Red") & (self.playerState["Button7"] == ""):
            self.playerState["Button7"] = self.baseState
            self.baseState = "Blue"
            print("B7")
            print(self.playerState)

            self.Button7.setIcon(QtGui.QIcon("img/redPlayer.png"))
            self.Button7.setIconSize(QtCore.QSize(140,140))
            self.Button7.toggle()
        
        elif self.Button7.isChecked() & (self.baseState == "Blue") & (self.playerState["Button7"] == ""):
            self.playerState["Button7"] = self.baseState
            self.baseState = "Red"
            print("B7")
            print(self.playerState)

            self.Button7.setIcon(QtGui.QIcon("img/bluePlayer.png"))
            self.Button7.setIconSize(QtCore.QSize(140,140))
            self.Button7.toggle()

        elif self.Button8.isChecked() & (self.baseState == "Red") & (self.playerState["Button8"] == ""):
            self.playerState["Button8"] = self.baseState
            self.baseState = "Blue"
            print("B8")
            print(self.playerState)

            self.Button8.setIcon(QtGui.QIcon("img/redPlayer.png"))
            self.Button8.setIconSize(QtCore.QSize(140,140))
            self.Button8.toggle()
        
        elif self.Button8.isChecked() & (self.baseState == "Blue") & (self.playerState["Button8"] == ""):
            self.playerState["Button8"] = self.baseState
            self.baseState = "Red"
            print("B8")
            print(self.playerState)

            self.Button8.setIcon(QtGui.QIcon("img/bluePlayer.png"))
            self.Button8.setIconSize(QtCore.QSize(140,140))
            self.Button8.toggle()

        elif self.Button9.isChecked() & (self.baseState == "Red") & (self.playerState["Button9"] == ""):
            self.playerState["Button9"] = self.baseState
            self.baseState = "Blue"
            print("B9")
            print(self.playerState)

            self.Button9.setIcon(QtGui.QIcon("img/redPlayer.png"))
            self.Button9.setIconSize(QtCore.QSize(140,140))
            self.Button9.toggle()
        
        elif self.Button9.isChecked() & (self.baseState == "Blue") & (self.playerState["Button9"] == ""):
            self.playerState["Button9"] = self.baseState
            self.baseState = "Red"
            print("B9")
            print(self.playerState)

            self.Button9.setIcon(QtGui.QIcon("img/bluePlayer.png"))
            self.Button9.setIconSize(QtCore.QSize(140,140))
            self.Button9.toggle()

        else:
            print("Already pressed!")
        


    def updateButtonLog(self):
        y=2
        # Need implementation
        
    def updateScore(self):
        x=2
        #Need implementation

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ScoreBlue.setMarkdown(_translate("MainWindow", "Score\n"
"\n"
""))
        self.ScoreBlue.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; color:#0000ff;\">Score</span></p></body></html>"))
        self.ScoreRed.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; color:#ff0000;\">Score</span></p></body></html>"))
        self.menuRestart.setTitle(_translate("MainWindow", "File"))
        self.actionRestart.setText(_translate("MainWindow", "Restart"))
        self.actionRestart.setStatusTip(_translate("MainWindow", "Restart the game"))
        self.actionRestart.setShortcut(_translate("MainWindow", "R"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
#     ui.updateUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
