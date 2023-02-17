from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
# from game import GameWindow

import game 


class WinnerWindow(QWidget):
    def __init__(self, winner):
        super().__init__()
        self.setWindowTitle("Winner")
        self.setGeometry(100, 100, 700, 500)
        self.label = QLabel(self)
        self.label.setText(f"{winner} wins the game !")
        self.label.move(100, 10)
        self.image_wins = QLabel(self)
        if winner == 'Computer':
            self.label.setStyleSheet("color: red;")
            pixmap = QPixmap("images/looser.jpg")
        else:
            self.label.setStyleSheet("color: green;")
            pixmap = QPixmap("images/winner.jpg")
        self.image_wins.setPixmap(pixmap)
        self.image_wins.move(50, 50)

        self.label.move(50, 50)
        
        # add a button to restart the game
        self.button = QPushButton("Restart", self)
        self.button.move(300, 450)
        self.button.clicked.connect(self.restartGame)

    def restartGame(self):
        self.close()
        self.window = game.GameWindow()
        self.window.show()