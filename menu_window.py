from PyQt5 import QtCore, QtGui, QtWidgets
from settings import *

class MenuWindow(QtWidgets.QMainWindow):
    font = QtGui.QFont()
    font.setFamily(FONT_NAME)

    twoPlayerRB_Signal = QtCore.pyqtSignal()
    easyCompRB_Signal = QtCore.pyqtSignal()
    goPlaySignal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.resize(X_WINDOW, Y_WINDOW)
        self.centralwidget = QtWidgets.QWidget(self)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.button_gridLayout = QtWidgets.QGridLayout()

        self.font.setPointSize(12)
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setMinimumSize(QtCore.QSize(0, 50))
        self.play_button.setFont(self.font)
        self.button_gridLayout.addWidget(self.play_button, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.button_gridLayout, 2, 0, 1, 1)

        self.main_gridLayout = QtWidgets.QGridLayout()
        self.main_gridLayout.setContentsMargins(25, -1, -1, -1)

        self.two_player_RB = QtWidgets.QRadioButton(self.centralwidget)
        self.two_player_RB.setFont(self.font)
        self.main_gridLayout.addWidget(self.two_player_RB, 0, 0, 1, 1)

        self.easy_comp_RB = QtWidgets.QRadioButton(self.centralwidget)
        self.easy_comp_RB.setFont(self.font)
        self.main_gridLayout.addWidget(self.easy_comp_RB, 1, 0, 1, 1)

        self.hard_comp_RB = QtWidgets.QRadioButton(self.centralwidget)
        self.hard_comp_RB.setFont(self.font)
        self.hard_comp_RB.setEnabled(False)
        self.main_gridLayout.addWidget(self.hard_comp_RB, 2, 0, 1, 1)

        self.gridLayout_2.addLayout(self.main_gridLayout, 1, 0, 1, 1)

        self.font.setPointSize(35)
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setMinimumSize(QtCore.QSize(0, 140))
        self.Title.setFont(self.font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Title, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.opponents = [self.two_player_RB, self.easy_comp_RB, self.hard_comp_RB]

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Tic-Tac-Toe"))
        self.play_button.setText(_translate("MainWindow", "Play"))
        self.two_player_RB.setText(_translate("MainWindow", "2-Player"))
        self.easy_comp_RB.setText(_translate("MainWindow", "Computer (Easy)"))
        self.hard_comp_RB.setText(_translate("MainWindow", "Computer (Hard)"))
        self.Title.setText(_translate("MainWindow", "Tic-Tac-Toe"))

        self.forEach_setSizePolicy(self.opponents, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.forEach_setSizePolicy([self.Title], QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.two_player_RB.clicked.connect(self.twoPlayerRB_Signal.emit)
        self.easy_comp_RB.clicked.connect(self.easyCompRB_Signal.emit)
        self.play_button.clicked.connect(self.goPlaySignal.emit)


    def forEach_setSizePolicy(self, vars: list, H: object, V: object) -> None:
        sizePolicy = QtWidgets.QSizePolicy(H, V)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        for name in vars:
            sizePolicy.setHeightForWidth(name.sizePolicy().hasHeightForWidth())
            name.setSizePolicy(sizePolicy)
