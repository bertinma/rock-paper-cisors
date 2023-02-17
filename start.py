from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
# from game import GameWindow
import game

class RockPaperScissorsWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window properties
        self.setGeometry(100, 100, 700, 500)
        self.setWindowTitle("Rock Paper Scissors")
        self.setStyleSheet("background-color: white; color: black;")

        # Set the label properties
        self.label = QLabel(self)
        self.label.setText("Hello !!\nLet's play Rock Paper Scissors")
        self.label.setAlignment(Qt.AlignCenter) # Center alignment
        self.label.move(0, 0)
        self.label.resize(700, 150)
        self.label.setStyleSheet("font-size: 24px;")

        # Set the button properties
        self.button = QPushButton(self)
        self.button.setText("Start")
        self.button.move(300, 200)
        self.button.resize(100, 50)
        self.button.setStyleSheet("background-color: black; color: white; font-size: 20px;")
        self.button.clicked.connect(self.start_game)

        # Set the image properties
        self.image = QLabel(self)
        pixmap = QPixmap("images/rpc.png")
        pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatio)
        self.image.setPixmap(pixmap)
        self.image.move(150, 300)



    def start_game(self):
        # Create a new game window
        self.game_window = game.GameWindow()
        self.game_window.show()
        self.close()