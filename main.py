from PyQt5 import QtWidgets
from functools import partial
from settings import *
import TicTacToe_Game
import menu_window
import sys, os

def suppress_qt_warnings():
   os.environ["QT_DEVICE_PIXEL_RATIO"] = "0"
   os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
   os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
   os.environ["QT_SCALE_FACTOR"] = "1"

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QtWidgets.QStackedWidget()
        self.stack.setMinimumSize(X_WINDOW, Y_WINDOW)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.stack)
        
        self.menuWindow = menu_window.MenuWindow()
        self.stack.addWidget(self.menuWindow)
        
        self.game = TicTacToe_Game.TicTacToe(opponent='twoplayer')
        self.stack.addWidget(self.game)

        self.menuWindow.twoPlayerRB_Signal.connect(self.twoPlayerSelect)
        self.menuWindow.easyCompRB_Signal.connect(self.easyCompSelect)
        self.stack.setCurrentWidget(self.menuWindow)

    def twoPlayerSelect(self):
        self.stack.removeWidget(self.game)
        self.game = TicTacToe_Game.TicTacToe(opponent='twoplayer')
        self.game.restart()
        self.stack.addWidget(self.game)
        self.menuWindow.goPlaySignal.connect(partial(self.stack.setCurrentWidget, self.game))
        self.game.goBackSignal.connect(partial(self.stack.setCurrentWidget, self.menuWindow))
    
    def easyCompSelect(self):
        self.stack.removeWidget(self.game)
        self.game = TicTacToe_Game.TicTacToe(opponent='easycomp')
        self.game.restart()
        self.stack.addWidget(self.game)
        self.menuWindow.goPlaySignal.connect(partial(self.stack.setCurrentWidget, self.game))
        self.game.goBackSignal.connect(partial(self.stack.setCurrentWidget, self.menuWindow))



if __name__ == '__main__':
    suppress_qt_warnings()
    app = QtWidgets.QApplication(sys.argv)
    w = MainWidget()
    w.resize(X_WINDOW, Y_WINDOW)

    # Move to the center of the screen
    screen = QtWidgets.QDesktopWidget().availableGeometry()
    middleWidth = screen.width() // 2
    middleHeight = screen.height() // 2
    centerPoint = (middleWidth - (X_WINDOW//2), middleHeight - (Y_WINDOW//2))
    w.move(*centerPoint)

    w.show()
    sys.exit(app.exec_())