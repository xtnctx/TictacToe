from PyQt5 import QtCore, QtGui, QtWidgets
from settings import *
import sys, os

btn_styleSheet = '''
    
    QPushButton {
        border-style: solid;
        border-width: 2px;
        border-radius: 15;
        border-color: black;
        padding: 4px
        }

    QPushButton::pressed {
        background-color : #D5D8DC
        }

'''

segment_styleSheet = '''

    QPushButton {
        border-style: solid;
        border-width: 2px;
        border-radius: 20px;
        border-color: #2471A3;
        padding: 4px
        }
        
    QPushButton::pressed {
        background-color : #D5D8DC
        }

'''

streak_styleSheet = '''

    QPushButton {
        color: black;
        background-color: #EC7063;
        border-style: solid;
        border-width: 2px;
        border-radius: 20px;
        border-color: black;
        padding: 4px
        }

'''

def suppress_qt_warnings():
   os.environ["QT_DEVICE_PIXEL_RATIO"] = "0"
   os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
   os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
   os.environ["QT_SCALE_FACTOR"] = "1"

class TicTacToe(QtWidgets.QMainWindow):
    '''
        Thank you for playing my simple game TicTacToe.
    '''
    font = QtGui.QFont()
    font.setFamily(FONT_NAME)
    font.setBold(True)
    font.setWeight(75)

    Player1_segments = []
    Player2_segments = []

    Player1_Turn = True

    def __init__(self):
        print(self.__doc__)
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(X_WINDOW, Y_WINDOW)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget.setObjectName("centralwidget")

        self.main_gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.main_gridLayout.setObjectName("main_gridLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(SEGMENT_GRID_SPACING)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.font.setPointSize(BTN_FONT_SIZE)

        self.home_btn = QtWidgets.QPushButton(self.centralwidget)
        self.home_btn.setMinimumSize(QtCore.QSize(0, 50))
        # self.home_btn.setShortcut(QtGui.QKeySequence("0"))
        self.home_btn.setFont(self.font)
        self.home_btn.setStyleSheet(btn_styleSheet)
        self.home_btn.setObjectName("home_btn")
        self.horizontalLayout.addWidget(self.home_btn)

        self.retry_btn = QtWidgets.QPushButton(self.centralwidget)
        self.retry_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.retry_btn.setFont(self.font)
        self.retry_btn.setStyleSheet(btn_styleSheet)
        self.retry_btn.setObjectName("retry_btn")
        self.horizontalLayout.addWidget(self.retry_btn)

        self.main_gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.segment0 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.segment0, 2, 0, 1, 1)

        self.segment1 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.segment1, 2, 1, 1, 1)

        self.segment2 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.segment2, 2, 2, 1, 1)

        self.segment3 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.segment3, 1, 0, 1, 1)

        self.segment4 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.segment4, 1, 1, 1, 1)

        self.segment5 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.segment5, 1, 2, 1, 1)

        self.segment6 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.segment6, 0, 0, 1, 1)

        self.segment7 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.segment7, 0, 1, 1, 1)

        self.segment8 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout_2.addWidget(self.segment8, 0, 2, 1, 1)

        self.btn_vars = [self.segment0, self.segment1, self.segment2,
                self.segment3, self.segment4, self.segment5,
                self.segment6, self.segment7, self.segment8]
        
        self.main_gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.statusBar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusBar)
        self.setCentralWidget(self.centralwidget)
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.home_btn.setText(_translate("MainWindow", "Back"))
        self.retry_btn.setText(_translate("MainWindow", "Restart"))
        self.statusBar.showMessage("Player1's Turn")

        self.forEach_setSizePolicy(self.btn_vars, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.forEach_setSizePolicy([self.centralwidget], QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.forEach_setSizePolicy([self.home_btn, self.retry_btn], QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        
        self.forEach_connectBtn(self.btn_vars)
        self.forEach_btnConfigure(self.btn_vars, self.font, QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.home_btn.clicked.connect(self.go_back)
        self.retry_btn.clicked.connect(self.restart)

    def forEach_setSizePolicy(self, vars: list, H: object, V: object) -> None:
        sizePolicy = QtWidgets.QSizePolicy(H, V)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        for name in vars:
            sizePolicy.setHeightForWidth(name.sizePolicy().hasHeightForWidth())
            name.setSizePolicy(sizePolicy)
    
    def forEach_btnConfigure(self, btn_vars: list, font: object, cursor: object) -> None:
        '''Configures segment's font, cursor, shortcut, and index'''
        font.setPointSize(SEGMENT_BTN_FONT_SIZE)
        for name in range(len(btn_vars)):
            btn_vars[name].setFont(font)
            btn_vars[name].setCursor(cursor)
            btn_vars[name].setObjectName(str(name)) # segment index
            btn_vars[name].setStyleSheet(segment_styleSheet)
            btn_vars[name].setShortcut(QtGui.QKeySequence(f"{name+1}"))


    def forEach_connectBtn(self, btn_vars: list) -> None:
        for name in btn_vars:
            name.clicked.connect(self.attack)
    
    def disable_segments(self, expt=list()) -> None:
        for name in self.btn_vars:
            if int(name.objectName()) not in expt:
                name.setEnabled(False) # Configuration restarts when using this :(
            else:
                name.setStyleSheet(streak_styleSheet)

    def attack(self):
        sending_button = self.sender()
        if self.Player1_Turn:
            if  sending_button.text() != PLAYER_IDS[0] and sending_button.text() != PLAYER_IDS[1]:
                self.Player1_Turn = False
                sending_button.setText(PLAYER_IDS[0])
                self.statusBar.showMessage("Player2's Turn")
                self.Player1_segments.append(int(sending_button.objectName()))
                Winner = self.checkWinner(self.Player1_segments)
                if Winner[0]:
                    self.statusBar.showMessage('Player1 Wins!')
                    self.disable_segments(expt=Winner[1])
        else:
            if sending_button.text() != PLAYER_IDS[0] and sending_button.text() != PLAYER_IDS[1]:
                self.Player1_Turn = True
                sending_button.setText(PLAYER_IDS[1])
                self.statusBar.showMessage("Player1's Turn")
                self.Player2_segments.append(int(sending_button.objectName()))
                Winner = self.checkWinner(self.Player2_segments)
                if Winner[0]:
                    self.statusBar.showMessage('Player2 Wins!')
                    self.disable_segments(expt=Winner[1])
        
        if self.isBoardFull():
            self.statusBar.showMessage('Draw')
            self.disable_segments()
    
    def isBoardFull(self):
        return len(self.Player1_segments + self.Player2_segments) == len(self.btn_vars)

    def checkWinner(self, player: int) -> list:
        for win in WINNING_MOVES:
            for i in range(len(win)):
                streak_idx = []
                streak = 0
                for choice in player:
                    if choice in win[i]:
                        streak_idx.append(choice)
                        streak += 1
                    if streak == 3: return [True, streak_idx]
        return [False]

    def go_back(self):
        window.setCurrentIndex(window.currentIndex()-1)

    def restart(self):
        for name in self.btn_vars:
            name.setEnabled(True)
            name.setText('')
            name.setStyleSheet(segment_styleSheet)
        self.Player1_segments = []
        self.Player2_segments = []
        self.Player1_Turn = True
        self.forEach_connectBtn(self.btn_vars)
        self.forEach_btnConfigure(self.btn_vars, self.font, QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statusBar.showMessage("Player1's Turn")

    def play(self) -> QtWidgets.QMainWindow:
        ''' 
        Use this when for standalone purposes
        '''
        print(self.__doc__)
        self.show()
    
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        font = QtGui.QFont()
        font.setFamily(FONT_NAME)
        font.setBold(False)
        font.setPointSize(12)
        font.setWeight(50)

        notify_user = QtWidgets.QMessageBox()
        notify_user.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        notify_user.setDefaultButton(QtWidgets.QMessageBox.No)
        notify_user.setIcon(QtWidgets.QMessageBox.Question)
        notify_user.setFont(font)
        notify_user.setText('Are you sure you want to quit?      ')
        notify_user.setWindowTitle("Quit Program")
        event.ignore()

        if notify_user.exec_() == QtWidgets.QMessageBox.Yes:
            event.accept()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == QtCore.Qt.Key_0:
            self.go_back()
        elif event.key() == QtCore.Qt.Key_Period:
            self.restart()
            
class UI_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget.setObjectName("centralwidget")

        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setText('next window')

        self.setCentralWidget(self.centralwidget)
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # self.setWindowTitle(_translate("MainWindow", "TicTacToe"))
        self.button.clicked.connect(self.play)
    
    def play(self):
        window.setCurrentIndex(window.currentIndex()+1)
        
        
if __name__ == "__main__":
    suppress_qt_warnings()
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QStackedWidget()

    MainWindow = UI_MainWindow()
    window.addWidget(MainWindow)

    game = TicTacToe()
    window.addWidget(game)

    window.setWindowTitle("TicTacToe")
    window.resize(X_WINDOW, Y_WINDOW)
    window.show()
    sys.exit(app.exec_())
