import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
import time
import random

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
        self.game_window = GameWindow()
        self.game_window.show()
        self.close()



class GameWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window properties
        self.setGeometry(100, 100, 700, 500)
        self.setWindowTitle("Game Window")
        self.setStyleSheet("background-color: white; color: black;")

        # Set the label properties
        self.label = QLabel(self)
        self.label.setText("Game Window")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.move(0, 0)
        self.label.resize(700, 150)
        self.label.setStyleSheet("font-size: 24px;")
        # self.show()

        # Set the input text box properties for player 1
        self.player1_label = QLabel(self)
        self.player1_label.setText("Player 1:")
        self.player1_label.move(50, 150)
        self.player1_label.setStyleSheet("font-size: 20px;")
        self.player1_input = QLineEdit(self)
        self.player1_input.move(150, 150)
        self.player1_input.resize(100, 30)
        self.player1_input.setStyleSheet("font-size: 20px;")

        # Set the input text box properties for player 2
        self.player2_label = QLabel(self)
        self.player2_label.setText("Player 2:")
        self.player2_label.move(450, 150)
        self.player2_label.setStyleSheet("font-size: 20px;")
        self.player2_input = QLineEdit(self)
        self.player2_input.move(550, 150)
        self.player2_input.resize(100, 30)
        self.player2_input.setStyleSheet("font-size: 20px;")
        self.player2_input.setText("Computer")

        # Create a list of image paths for rock, paper, and scissors
        self.images = ["rock.png", "paper.png", "scissors.png"]
        self.image_index = 0

        # display rotativly the three images until a keyboard event 
        # is triggered
        # Display them on left and on the right of the window 
        # (one for each player)
        self.quit_loop = False
        self.display_image()

    def display_image(self):
        self.image1 = QLabel(self)
        self.image2 = QLabel(self)
        if not self.quit_loop:
            timer = QTimer(self)
            timer.timeout.connect(self.updateImage)
            timer.start(.3*1000)
            self.updateImage()

    def updateImage(self):
        pixmap = QPixmap("images/" + self.images[self.image_index])
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
        self.image1.setPixmap(pixmap)
        self.image1.move(75, 250)
        pixmap = QPixmap("images/" + self.images[self.image_index + 1 if self.image_index < 2 else 0])
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
        self.image2.setPixmap(pixmap)
        self.image2.move(475, 250)
        self.image_index += 1
        self.image_index %= 3


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.player1_input.setReadOnly(True)
            self.player2_input.setReadOnly(True)
        if event.key() in [Qt.Key_Escape, Qt.Key_Q, Qt.Key_S, Qt.Key_D]:
            self.quit_loop = True 
        if event.key() == Qt.Key_Q:
            self.image_index = 0
        elif event.key() == Qt.Key_S:
            self.image_index = 1
        elif event.key() == Qt.Key_D:
            self.image_index = 2

        # select random in between 0 and 2
        self.image_index_computer = random.randint(0, 2)

        

    def update_scores(self):
        # Update the scores of the players
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RockPaperScissorsWindow()
    window.show()
    sys.exit(app.exec_())