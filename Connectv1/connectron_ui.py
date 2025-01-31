
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSlider, QStackedWidget,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(798, 534)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(480, 480))
        MainWindow.setStyleSheet(u"background-color: #BFCDE0;color: #000000;")
        self.actionSave_Game_State_as = QAction(MainWindow)
        self.actionSave_Game_State_as.setObjectName(u"actionSave_Game_State_as")
        self.action_SaveGame = QAction(MainWindow)
        self.action_SaveGame.setObjectName(u"action_SaveGame")
        self.action_EndRound = QAction(MainWindow)
        self.action_EndRound.setObjectName(u"action_EndRound")
        self.action_EndGame = QAction(MainWindow)
        self.action_EndGame.setObjectName(u"action_EndGame")
        self.action_NewGame = QAction(MainWindow)
        self.action_NewGame.setObjectName(u"action_NewGame")
        self.actionInfinite_Overflow = QAction(MainWindow)
        self.actionInfinite_Overflow.setObjectName(u"actionInfinite_Overflow")
        self.actionGray_Tile_Indicator = QAction(MainWindow)
        self.actionGray_Tile_Indicator.setObjectName(u"actionGray_Tile_Indicator")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_Title = QFrame(self.centralwidget)
        self.frame_Title.setObjectName(u"frame_Title")
        self.frame_Title.setGeometry(QRect(320, 0, 161, 51))
        self.frame_Title.setStyleSheet(u"background-color: #DFE6F0;color: #000000;")
        self.frame_Title.setFrameShape(QFrame.StyledPanel)
        self.frame_Title.setFrameShadow(QFrame.Raised)
        self.label_Title = QLabel(self.frame_Title)
        self.label_Title.setObjectName(u"label_Title")
        self.label_Title.setGeometry(QRect(20, 10, 131, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(24)
        self.label_Title.setFont(font)
        self.label_Title.setFrameShape(QFrame.NoFrame)
        self.label_Title.setLineWidth(4)
        self.frame_Board = QFrame(self.centralwidget)
        self.frame_Board.setObjectName(u"frame_Board")
        self.frame_Board.setGeometry(QRect(20, 80, 400, 400))
        self.frame_Board.setMinimumSize(QSize(400, 400))
        self.frame_Board.setStyleSheet(u"background-color: #DFE6F0;color: #000000;")
        self.gridLayoutWidget = QWidget(self.frame_Board)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 401, 401))
        self.gridLayout_Board = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_Board.setObjectName(u"gridLayout_Board")
        self.gridLayout_Board.setContentsMargins(0, 0, 0, 0)
        self.frame_Stacked = QFrame(self.centralwidget)
        self.frame_Stacked.setObjectName(u"frame_Stacked")
        self.frame_Stacked.setGeometry(QRect(450, 80, 311, 401))
        self.frame_Stacked.setStyleSheet(u"background-color: #DFE6F0;color: #000000;")
        self.frame_Stacked.setFrameShape(QFrame.StyledPanel)
        self.frame_Stacked.setFrameShadow(QFrame.Raised)
        self.stackedWidget_Menu = QStackedWidget(self.frame_Stacked)
        self.stackedWidget_Menu.setObjectName(u"stackedWidget_Menu")
        self.stackedWidget_Menu.setGeometry(QRect(0, 0, 311, 401))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.pushButton_NewGame = QPushButton(self.page)
        self.pushButton_NewGame.setObjectName(u"pushButton_NewGame")
        self.pushButton_NewGame.setGeometry(QRect(30, 330, 251, 51))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(18)
        self.pushButton_NewGame.setFont(font1)
        self.pushButton_NewGame.setStyleSheet(u"background-color: #EBF3F5;color: #000000;")
        self.label_GameSettings = QLabel(self.page)
        self.label_GameSettings.setObjectName(u"label_GameSettings")
        self.label_GameSettings.setGeometry(QRect(40, 20, 111, 21))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(16)
        self.label_GameSettings.setFont(font2)
        self.frame_BoardWidth = QFrame(self.page)
        self.frame_BoardWidth.setObjectName(u"frame_BoardWidth")
        self.frame_BoardWidth.setGeometry(QRect(30, 60, 251, 71))
        self.frame_BoardWidth.setStyleSheet(u"background-color: #EBF3F5;color: #000000;")
        self.frame_BoardWidth.setFrameShape(QFrame.StyledPanel)
        self.frame_BoardWidth.setFrameShadow(QFrame.Raised)
        self.horizontalSlider_BoardWidth = QSlider(self.frame_BoardWidth)
        self.horizontalSlider_BoardWidth.setObjectName(u"horizontalSlider_BoardWidth")
        self.horizontalSlider_BoardWidth.setGeometry(QRect(110, 40, 121, 25))
        self.horizontalSlider_BoardWidth.setStyleSheet(u"QSlider::groove:horizontal { background: #bfcde0; height: 6px; border-radius: 3px; } QSlider::handle:horizontal { background: #626F89; width: 14px; height: 14px; border-radius: 7px; margin: -4px 0; }")
        self.horizontalSlider_BoardWidth.setOrientation(Qt.Horizontal)
        self.label_BoardWidth = QLabel(self.frame_BoardWidth)
        self.label_BoardWidth.setObjectName(u"label_BoardWidth")
        self.label_BoardWidth.setGeometry(QRect(20, 10, 81, 41))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(14)
        self.label_BoardWidth.setFont(font3)
        self.plainTextEdit_BoardWidth = QPlainTextEdit(self.frame_BoardWidth)
        self.plainTextEdit_BoardWidth.setObjectName(u"plainTextEdit_BoardWidth")
        self.plainTextEdit_BoardWidth.setGeometry(QRect(160, 10, 71, 31))
        self.plainTextEdit_BoardWidth.setFont(font3)
        self.frame_BoardHeight = QFrame(self.page)
        self.frame_BoardHeight.setObjectName(u"frame_BoardHeight")
        self.frame_BoardHeight.setGeometry(QRect(30, 150, 251, 71))
        self.frame_BoardHeight.setStyleSheet(u"background-color: #EBF3F5;color: #000000;")
        self.frame_BoardHeight.setFrameShape(QFrame.StyledPanel)
        self.frame_BoardHeight.setFrameShadow(QFrame.Raised)
        self.horizontalSlider_BoardHeight = QSlider(self.frame_BoardHeight)
        self.horizontalSlider_BoardHeight.setObjectName(u"horizontalSlider_BoardHeight")
        self.horizontalSlider_BoardHeight.setGeometry(QRect(110, 40, 121, 25))
        self.horizontalSlider_BoardHeight.setStyleSheet(u"QSlider::groove:horizontal { background: #bfcde0; height: 6px; border-radius: 3px; } QSlider::handle:horizontal { background: #626F89; width: 14px; height: 14px; border-radius: 7px; margin: -4px 0; }")
        self.horizontalSlider_BoardHeight.setOrientation(Qt.Horizontal)
        self.label_BoardHeight = QLabel(self.frame_BoardHeight)
        self.label_BoardHeight.setObjectName(u"label_BoardHeight")
        self.label_BoardHeight.setGeometry(QRect(20, 10, 81, 41))
        self.label_BoardHeight.setFont(font3)
        self.plainTextEdit_BoardHeight = QPlainTextEdit(self.frame_BoardHeight)
        self.plainTextEdit_BoardHeight.setObjectName(u"plainTextEdit_BoardHeight")
        self.plainTextEdit_BoardHeight.setGeometry(QRect(160, 10, 71, 31))
        self.plainTextEdit_BoardHeight.setFont(font3)
        self.frame_PlayerCount = QFrame(self.page)
        self.frame_PlayerCount.setObjectName(u"frame_PlayerCount")
        self.frame_PlayerCount.setGeometry(QRect(30, 240, 251, 71))
        self.frame_PlayerCount.setStyleSheet(u"background-color: #EBF3F5;color: #000000;")
        self.frame_PlayerCount.setFrameShape(QFrame.StyledPanel)
        self.frame_PlayerCount.setFrameShadow(QFrame.Raised)
        self.horizontalSlider_PlayerCount = QSlider(self.frame_PlayerCount)
        self.horizontalSlider_PlayerCount.setObjectName(u"horizontalSlider_PlayerCount")
        self.horizontalSlider_PlayerCount.setGeometry(QRect(110, 40, 121, 25))
        self.horizontalSlider_PlayerCount.setStyleSheet(u"QSlider::groove:horizontal { background: #bfcde0; height: 6px; border-radius: 3px; } QSlider::handle:horizontal { background: #626F89; width: 14px; height: 14px; border-radius: 7px; margin: -4px 0; }")
        self.horizontalSlider_PlayerCount.setOrientation(Qt.Horizontal)
        self.label_PlayerCount = QLabel(self.frame_PlayerCount)
        self.label_PlayerCount.setObjectName(u"label_PlayerCount")
        self.label_PlayerCount.setGeometry(QRect(20, 10, 81, 41))
        self.label_PlayerCount.setFont(font3)
        self.plainTextEdit_PlayerCount = QPlainTextEdit(self.frame_PlayerCount)
        self.plainTextEdit_PlayerCount.setObjectName(u"plainTextEdit_PlayerCount")
        self.plainTextEdit_PlayerCount.setGeometry(QRect(160, 10, 71, 31))
        self.plainTextEdit_PlayerCount.setFont(font3)
        self.stackedWidget_Menu.addWidget(self.page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_GameSettings2 = QLabel(self.page_4)
        self.label_GameSettings2.setObjectName(u"label_GameSettings2")
        self.label_GameSettings2.setGeometry(QRect(40, 20, 111, 21))
        self.label_GameSettings2.setFont(font2)
        self.frame_RoundNum = QFrame(self.page_4)
        self.frame_RoundNum.setObjectName(u"frame_RoundNum")
        self.frame_RoundNum.setGeometry(QRect(30, 150, 251, 91))
        self.frame_RoundNum.setStyleSheet(u"background-color: #EBF3F5;color: #000000;")
        self.frame_RoundNum.setFrameShape(QFrame.StyledPanel)
        self.frame_RoundNum.setFrameShadow(QFrame.Raised)
        self.label_Rounds = QLabel(self.frame_RoundNum)
        self.label_Rounds.setObjectName(u"label_Rounds")
        self.label_Rounds.setGeometry(QRect(20, 10, 51, 21))
        self.label_Rounds.setFont(font3)
        self.plainTextEdit_RoundNum = QPlainTextEdit(self.frame_RoundNum)
        self.plainTextEdit_RoundNum.setObjectName(u"plainTextEdit_RoundNum")
        self.plainTextEdit_RoundNum.setGeometry(QRect(120, 40, 71, 31))
        self.plainTextEdit_RoundNum.setFont(font3)
        self.comboBox_Rounds = QComboBox(self.frame_RoundNum)
        self.comboBox_Rounds.addItem("")
        self.comboBox_Rounds.addItem("")
        self.comboBox_Rounds.setObjectName(u"comboBox_Rounds")
        self.comboBox_Rounds.setGeometry(QRect(20, 40, 91, 32))
        self.frame_WinningLength = QFrame(self.page_4)
        self.frame_WinningLength.setObjectName(u"frame_WinningLength")
        self.frame_WinningLength.setGeometry(QRect(30, 60, 251, 71))
        self.frame_WinningLength.setStyleSheet(u"background-color: #EBF3F5;color: #000000;")
        self.frame_WinningLength.setFrameShape(QFrame.StyledPanel)
        self.frame_WinningLength.setFrameShadow(QFrame.Raised)
        self.horizontalSlider_WinningLength = QSlider(self.frame_WinningLength)
        self.horizontalSlider_WinningLength.setObjectName(u"horizontalSlider_WinningLength")
        self.horizontalSlider_WinningLength.setGeometry(QRect(170, 40, 61, 25))
        self.horizontalSlider_WinningLength.setStyleSheet(u"QSlider::groove:horizontal { background: #bfcde0; height: 6px; border-radius: 3px; } QSlider::handle:horizontal { background: #626F89; width: 14px; height: 14px; border-radius: 7px; margin: -4px 0; }")
        self.horizontalSlider_WinningLength.setOrientation(Qt.Horizontal)
        self.label_WinningLength = QLabel(self.frame_WinningLength)
        self.label_WinningLength.setObjectName(u"label_WinningLength")
        self.label_WinningLength.setGeometry(QRect(20, 10, 131, 41))
        self.label_WinningLength.setFont(font3)
        self.plainTextEdit_WinningLength = QPlainTextEdit(self.frame_WinningLength)
        self.plainTextEdit_WinningLength.setObjectName(u"plainTextEdit_WinningLength")
        self.plainTextEdit_WinningLength.setGeometry(QRect(160, 10, 71, 31))
        self.plainTextEdit_WinningLength.setFont(font3)
        self.label_WinningLength.raise_()
        self.horizontalSlider_WinningLength.raise_()
        self.plainTextEdit_WinningLength.raise_()
        self.pushButton_NewGame_2 = QPushButton(self.page_4)
        self.pushButton_NewGame_2.setObjectName(u"pushButton_NewGame_2")
        self.pushButton_NewGame_2.setGeometry(QRect(30, 330, 251, 51))
        self.pushButton_NewGame_2.setFont(font1)
        self.pushButton_NewGame_2.setStyleSheet(u"background-color: #EBF3F5;color: #000000;")
        self.stackedWidget_Menu.addWidget(self.page_4)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_AlliancesTitle = QLabel(self.page_2)
        self.label_AlliancesTitle.setObjectName(u"label_AlliancesTitle")
        self.label_AlliancesTitle.setGeometry(QRect(40, 20, 71, 21))
        self.label_AlliancesTitle.setFont(font2)
        self.listWidget_Alliances = QListWidget(self.page_2)
        self.listWidget_Alliances.setObjectName(u"listWidget_Alliances")
        self.listWidget_Alliances.setGeometry(QRect(40, 50, 231, 192))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(13)
        self.listWidget_Alliances.setFont(font4)
        self.listWidget_Alliances.setStyleSheet(u"background-color: #EBF3F5;color: #000000;")
        self.pushButton_NewAlliance = QPushButton(self.page_2)
        self.pushButton_NewAlliance.setObjectName(u"pushButton_NewAlliance")
        self.pushButton_NewAlliance.setGeometry(QRect(30, 260, 111, 31))
        self.pushButton_NewAlliance.setFont(font2)
        self.pushButton_NewAlliance.setStyleSheet(u"background-color: #EBF3F5;color: #000000;")
        self.label_Alliances0 = QLabel(self.page_2)
        self.label_Alliances0.setObjectName(u"label_Alliances0")
        self.label_Alliances0.setGeometry(QRect(30, 300, 71, 16))
        self.label_Alliances0.setFont(font3)
        self.label_Alliances1 = QLabel(self.page_2)
        self.label_Alliances1.setObjectName(u"label_Alliances1")
        self.label_Alliances1.setGeometry(QRect(160, 300, 71, 16))
        self.label_Alliances1.setFont(font3)
        self.pushButton_StartGame = QPushButton(self.page_2)
        self.pushButton_StartGame.setObjectName(u"pushButton_StartGame")
        self.pushButton_StartGame.setGeometry(QRect(30, 330, 251, 51))
        self.pushButton_StartGame.setFont(font2)
        self.pushButton_StartGame.setStyleSheet(u"background-color: #EBF3F5;color: #000000;")
        self.comboBox_Player = QComboBox(self.page_2)
        self.comboBox_Player.setObjectName(u"comboBox_Player")
        self.comboBox_Player.setGeometry(QRect(100, 300, 51, 21))
        self.comboBox_Alliance = QComboBox(self.page_2)
        self.comboBox_Alliance.setObjectName(u"comboBox_Alliance")
        self.comboBox_Alliance.setGeometry(QRect(230, 300, 51, 21))
        self.pushButton_DeleteAlliance = QPushButton(self.page_2)
        self.pushButton_DeleteAlliance.setObjectName(u"pushButton_DeleteAlliance")
        self.pushButton_DeleteAlliance.setGeometry(QRect(160, 260, 61, 31))
        self.pushButton_DeleteAlliance.setFont(font2)
        self.pushButton_DeleteAlliance.setStyleSheet(u"background-color: #EBF3F5;color: #000000;")
        self.comboBox_DeleteAlliance = QComboBox(self.page_2)
        self.comboBox_DeleteAlliance.setObjectName(u"comboBox_DeleteAlliance")
        self.comboBox_DeleteAlliance.setGeometry(QRect(230, 260, 51, 32))
        self.stackedWidget_Menu.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_Game = QLabel(self.page_3)
        self.label_Game.setObjectName(u"label_Game")
        self.label_Game.setGeometry(QRect(40, 20, 51, 21))
        self.label_Game.setFont(font2)
        self.checkBox_Bomb = QCheckBox(self.page_3)
        self.checkBox_Bomb.setObjectName(u"checkBox_Bomb")
        self.checkBox_Bomb.setGeometry(QRect(40, 120, 85, 20))
        self.checkBox_Bomb.setFont(font3)
        self.checkBox_Bomb.setStyleSheet(u"")
        self.label_CurrentMove = QLabel(self.page_3)
        self.label_CurrentMove.setObjectName(u"label_CurrentMove")
        self.label_CurrentMove.setGeometry(QRect(40, 70, 161, 21))
        self.label_CurrentMove.setFont(font3)
        self.frame_Counter = QFrame(self.page_3)
        self.frame_Counter.setObjectName(u"frame_Counter")
        self.frame_Counter.setGeometry(QRect(210, 70, 20, 20))
        self.frame_Counter.setStyleSheet(u"background-color: #FF0000;\n"
"border: none;\n"
"border-radius: 10px;")
        self.frame_Counter.setFrameShape(QFrame.StyledPanel)
        self.frame_Counter.setFrameShadow(QFrame.Raised)
        self.stackedWidget_Menu.addWidget(self.page_3)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_Result = QLabel(self.page_5)
        self.label_Result.setObjectName(u"label_Result")
        self.label_Result.setGeometry(QRect(40, 20, 51, 21))
        self.label_Result.setFont(font2)
        self.listWidget = QListWidget(self.page_5)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(40, 60, 231, 192))
        self.stackedWidget_Menu.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.listWidget_ChangeAlliances = QListWidget(self.page_6)
        self.listWidget_ChangeAlliances.setObjectName(u"listWidget_ChangeAlliances")
        self.listWidget_ChangeAlliances.setGeometry(QRect(40, 50, 231, 192))
        self.listWidget_ChangeAlliances.setFont(font4)
        self.listWidget_ChangeAlliances.setStyleSheet(u"background-color: #EBF3F5;color: #000000;")
        self.label_Result_2 = QLabel(self.page_6)
        self.label_Result_2.setObjectName(u"label_Result_2")
        self.label_Result_2.setGeometry(QRect(40, 20, 141, 21))
        self.label_Result_2.setFont(font2)
        self.stackedWidget_Menu.addWidget(self.page_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 798, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName(u"menuGame")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuAdvanced_Game_Options = QMenu(self.menuOptions)
        self.menuAdvanced_Game_Options.setObjectName(u"menuAdvanced_Game_Options")
        self.menuGraphics = QMenu(self.menuOptions)
        self.menuGraphics.setObjectName(u"menuGraphics")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuFile.addAction(self.action_SaveGame)
        self.menuGame.addAction(self.action_EndRound)
        self.menuGame.addAction(self.action_EndGame)
        self.menuGame.addAction(self.action_NewGame)
        self.menuOptions.addAction(self.menuAdvanced_Game_Options.menuAction())
        self.menuOptions.addAction(self.menuGraphics.menuAction())
        self.menuAdvanced_Game_Options.addAction(self.actionInfinite_Overflow)
        self.menuGraphics.addAction(self.actionGray_Tile_Indicator)

        self.retranslateUi(MainWindow)

        self.stackedWidget_Menu.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave_Game_State_as.setText(QCoreApplication.translate("MainWindow", u"Save Game State as", None))
        self.action_SaveGame.setText(QCoreApplication.translate("MainWindow", u"Save Game State", None))
        self.action_EndRound.setText(QCoreApplication.translate("MainWindow", u"End Current Round", None))
        self.action_EndGame.setText(QCoreApplication.translate("MainWindow", u"End Game", None))
        self.action_NewGame.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.actionInfinite_Overflow.setText(QCoreApplication.translate("MainWindow", u"Infinite Overflow", None))
        self.actionGray_Tile_Indicator.setText(QCoreApplication.translate("MainWindow", u"Gray Tile Indicator", None))
        self.label_Title.setText(QCoreApplication.translate("MainWindow", u"Connectron", None))
        self.pushButton_NewGame.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.label_GameSettings.setText(QCoreApplication.translate("MainWindow", u"Game Settings", None))
        self.label_BoardWidth.setText(QCoreApplication.translate("MainWindow", u"Board Width\n"
"6-100", None))
        self.plainTextEdit_BoardWidth.setPlainText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_BoardHeight.setText(QCoreApplication.translate("MainWindow", u"Board Height\n"
"6-100", None))
        self.plainTextEdit_BoardHeight.setPlainText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_PlayerCount.setText(QCoreApplication.translate("MainWindow", u"Player Count\n"
"0-10", None))
        self.plainTextEdit_PlayerCount.setPlainText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_GameSettings2.setText(QCoreApplication.translate("MainWindow", u"Game Settings", None))
        self.label_Rounds.setText(QCoreApplication.translate("MainWindow", u"Rounds", None))
        self.plainTextEdit_RoundNum.setPlainText(QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_Rounds.setItemText(0, QCoreApplication.translate("MainWindow", u"First to", None))
        self.comboBox_Rounds.setItemText(1, QCoreApplication.translate("MainWindow", u"Best of", None))

        self.label_WinningLength.setText(QCoreApplication.translate("MainWindow", u"Winning Line Length\n"
"4-10", None))
        self.plainTextEdit_WinningLength.setPlainText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_NewGame_2.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_AlliancesTitle.setText(QCoreApplication.translate("MainWindow", u"Alliances", None))
        self.pushButton_NewAlliance.setText(QCoreApplication.translate("MainWindow", u"New Alliance", None))
        self.label_Alliances0.setText(QCoreApplication.translate("MainWindow", u"add Player", None))
        self.label_Alliances1.setText(QCoreApplication.translate("MainWindow", u"to Alliance", None))
        self.pushButton_StartGame.setText(QCoreApplication.translate("MainWindow", u"Start Game", None))
        self.pushButton_DeleteAlliance.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_Game.setText(QCoreApplication.translate("MainWindow", u"Game", None))
        self.checkBox_Bomb.setText(QCoreApplication.translate("MainWindow", u"Bomb?", None))
        self.label_CurrentMove.setText(QCoreApplication.translate("MainWindow", u"Current Move is Player", None))
        self.label_Result.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.label_Result_2.setText(QCoreApplication.translate("MainWindow", u"Change Alliances?", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuAdvanced_Game_Options.setTitle(QCoreApplication.translate("MainWindow", u"Advanced Game Options", None))
        self.menuGraphics.setTitle(QCoreApplication.translate("MainWindow", u"Graphics", None))
    # retranslateUi

