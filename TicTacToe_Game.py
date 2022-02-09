from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
from settings import *
import random
import time



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
    Computer_segments = []

    Player1_Turn = True
    Computer_choices = list(range(9))
    hasWinner = False

    goBackSignal = QtCore.pyqtSignal()

    def __init__(self, opponent='twoPlayer'):
        print(self.__doc__)
        super().__init__()
        self.opponent = opponent
        self.resize(X_WINDOW, Y_WINDOW)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.main_gridLayout = QtWidgets.QGridLayout(self.centralwidget)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(SEGMENT_GRID_SPACING)

        self.font.setPointSize(BTN_FONT_SIZE)

        self.home_btn = QtWidgets.QPushButton(self.centralwidget)
        self.home_btn.setMinimumSize(QtCore.QSize(0, BTN_V_MIN))
        self.home_btn.setFont(self.font)
        self.home_btn.setStyleSheet(btn_styleSheet)
        self.horizontalLayout.addWidget(self.home_btn)

        self.retry_btn = QtWidgets.QPushButton(self.centralwidget)
        self.retry_btn.setMinimumSize(QtCore.QSize(0, BTN_V_MIN))
        self.retry_btn.setFont(self.font)
        self.retry_btn.setStyleSheet(btn_styleSheet)
        self.horizontalLayout.addWidget(self.retry_btn)

        self.main_gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setColumnMinimumWidth(0, X_WINDOW)
        self.gridLayout_2.setColumnMinimumWidth(1, X_WINDOW)
        self.gridLayout_2.setColumnMinimumWidth(2, X_WINDOW)

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
            if self.opponent.lower() == 'twoplayer':
                name.clicked.connect(self.two_player_attack)
            elif self.opponent.lower() == 'easycomp':
                name.clicked.connect(self.easy_computer_attack)
    
    def disable_segments(self, expt=list()) -> None:
        for name in self.btn_vars:
            if int(name.objectName()) not in expt:
                name.setEnabled(False) # Configuration restarts when using this :(
            else:
                name.setStyleSheet(streak_styleSheet)

    def two_player_attack(self):
        sending_button = self.sender()
        if self.Player1_Turn:
            if  sending_button.text() != PLAYER_IDS[0] and sending_button.text() != PLAYER_IDS[1]:
                sending_button.setText(PLAYER_IDS[0])
                self.statusBar.showMessage("Player2's Turn")
                self.Player1_segments.append(int(sending_button.objectName()))
                Winner = self.checkWinner(self.Player1_segments)
                self.Player1_Turn = False
                if Winner[0]:
                    self.statusBar.showMessage('Player1 Wins!')
                    self.disable_segments(expt=Winner[1])
        else:
            if sending_button.text() != PLAYER_IDS[0] and sending_button.text() != PLAYER_IDS[1]:
                sending_button.setText(PLAYER_IDS[1])
                self.statusBar.showMessage("Player1's Turn")
                self.Player2_segments.append(int(sending_button.objectName()))
                Winner = self.checkWinner(self.Player2_segments)
                self.Player1_Turn = True
                if Winner[0]:
                    self.statusBar.showMessage('Player2 Wins!')
                    self.disable_segments(expt=Winner[1])
        
        if self.isBoardFull():
            self.statusBar.showMessage('Draw')
            self.disable_segments()

    def easy_computer_attack(self):
        sending_button = self.sender()
        if self.Player1_Turn and not self.hasWinner: # Human Attack
            if  sending_button.text() != PLAYER_IDS[0] and sending_button.text() != PLAYER_IDS[1]:
                sending_button.setText(PLAYER_IDS[0])
                self.statusBar.showMessage("Computer's Turn")
                self.Player1_segments.append(int(sending_button.objectName()))
                self.Computer_choices.remove(int(sending_button.objectName()))
                Winner = self.checkWinner(self.Player1_segments)
                self.Player1_Turn = False

                if Winner[0]:
                    self.statusBar.showMessage('Player1 Wins!')
                    self.disable_segments(expt=Winner[1])
                    self.hasWinner = True

                elif self.isBoardFull():
                    self.statusBar.showMessage('Draw')
                    self.disable_segments()
                    self.hasWinner = 1

                computer_move = Thread(target=self.computer_time)
                computer_move.start()

    def computer_time(self):
        if not self.hasWinner:
            computer_choice = random.choice(self.Computer_choices)
            for name in self.btn_vars:
                if name.objectName() == str(computer_choice):
                    time.sleep(random.choice(list(range(1, 3))))
                    name.setText(PLAYER_IDS[1])
                    self.statusBar.showMessage("Player1's Turn")
                    self.Computer_segments.append(computer_choice)
                    self.Computer_choices.remove(computer_choice)
                    self.Player1_Turn = True
                    print(computer_choice)
                    break
            Winner = self.checkWinner(self.Computer_segments)
            if Winner[0]:
                self.statusBar.showMessage('Computer Wins!')
                self.disable_segments(expt=Winner[1])
                self.hasWinner = True

            elif self.isBoardFull():
                self.statusBar.showMessage('Draw')
                self.disable_segments()

    def isBoardFull(self):
        if self.opponent.lower() == 'twoplayer':
            return len(self.Player1_segments + self.Player2_segments) == len(self.btn_vars)
        elif self.opponent.lower() == 'easycomp':
            return len(self.Player1_segments + self.Computer_segments) == len(self.btn_vars)
    
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
        self.restart()
        self.goBackSignal.emit()
        
    def restart(self):
        for name in self.btn_vars:
            name.setEnabled(True)
            name.setText('')
            name.setStyleSheet(segment_styleSheet)
        self.Player1_segments = []
        self.Player2_segments = []
        self.Computer_segments = []
        self.Computer_choices = list(range(9))
        self.Player1_Turn = True
        self.hasWinner = False
        self.forEach_connectBtn(self.btn_vars)
        self.forEach_btnConfigure(self.btn_vars, self.font, QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.statusBar.showMessage("Player1's Turn")

    def play(self) -> QtWidgets.QMainWindow:
        ''' 
        Use this for standalone purposes
        '''
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

