import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
import time
import random
from pathlib import Path

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
        self.images = ["rock.png", "scissors.png", "paper.png"]
        self.image_index = 0
        self.image_index_computer = None 
        # display rotativly the three images until a keyboard event 
        # is triggered
        # Display them on left and on the right of the window 
        # (one for each player)
        self.display_image()

    def display_image(self):
        self.image1 = QLabel(self)
        self.image2 = QLabel(self)
        self.timer = QTimer(self)
        self.textResult = QLabel(self)
        self.timer.timeout.connect(self.updateImage)
        self.timer.start(300)
        self.updateImage()

    def updateImage(self):
        pixmap = QPixmap("images/" + self.images[self.image_index])
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
        self.image1.setPixmap(pixmap)
        self.image1.move(75, 250)
        if self.image_index_computer is None:
            self.image_index_computer = self.image_index + 1 if self.image_index < 2 else 0
            self.image_index += 1
            self.image_index %= 3
        pixmap = QPixmap("images/" + self.images[self.image_index_computer])
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
        self.image2.setPixmap(pixmap)
        self.image2.move(475, 250)
        self.image_index_computer = None


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.player1_input.setReadOnly(True)
            self.player2_input.setReadOnly(True)
        elif event.key() == Qt.Key_M:
            self.player1_input.setReadOnly(False)
            self.player2_input.setReadOnly(False)
        else:
            # select random in between 0 and 2 included
            self.image_index_computer = random.randint(0, 2)
            pcr_str = " ".join([Path(self.images[i]).stem for i in range(3)])
            print(pcr_str)
            print(f"Key pressed:  {event.text()} {Path(self.images[self.image_index]).stem}")
            print(f'Computer choice: {self.image_index_computer} {Path(self.images[self.image_index_computer]).stem}')
            if event.key() in [Qt.Key_Escape, Qt.Key_Q, Qt.Key_S, Qt.Key_D]:
                self.timer.disconnect()
                print(f"Quit loop !")
            if event.key() == Qt.Key_Q:
                self.image_index = 0
            elif event.key() == Qt.Key_S:
                self.image_index = 1
            elif event.key() == Qt.Key_D:
                self.image_index = 2
            self.displayResults()
            self.updateScores()
            self.updateImage()
            time.sleep(3)
            self.show()
            self.timer.timeout.connect(self.updateImage)

    def displayResults(self):
        # Display the results of the game
        self.textResult.move(250, 480)
        self.textResult.setStyleSheet("background: red;")
        print(f"image_index: {self.image_index}")
        print(f"image_index_computer: {self.image_index_computer}")

        if self.image_index == self.image_index_computer:
            self.textResult.setText("Draw")
            print("Draw")
        elif (self.image_index + 1) % 3 == self.image_index_computer:
            self.textResult.setText(f" {self.player1_input.text()} wins")
            print(f" {self.player1_input.text()} wins")
            # write text in green color
            self.textResult.setStyleSheet("color: green;")

        else:
            self.textResult.setText(f" {self.player2_input.text()} wins")
            print(f" {self.player2_input.text()} wins")
            # write text in red color
            self.textResult.setStyleSheet("color: red;")
        print("\n\n\n")
        

    def updateScores(self):
        # Update the scores of the players
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RockPaperScissorsWindow()
    window.show()
    sys.exit(app.exec_())