from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit
import random

# from results import WinnerWindow
import results

class GameWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.winner_window = None
        # Set the window properties
        self.setGeometry(100, 100, 700, 500)
        self.setWindowTitle("Game Window")
        self.setStyleSheet("background-color: white; color: black;")

        # players score 
        self.player1_score = 0
        self.player2_score = 0
        self.winner = ""

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

        self.point_image_1 = QLabel(self)
        self.point_image_2 = QLabel(self)
        self.point_image_3 = QLabel(self)
        self.point_image_4 = QLabel(self)
        self.point_image_5 = QLabel(self)
        self.point_image_6 = QLabel(self)

        pixmap = QPixmap("images/null.png").scaled(32, 32, Qt.KeepAspectRatio)
        self.point_image_1.setPixmap(pixmap)
        self.point_image_1.move(75, 190)
        self.point_image_1.show()
        self.point_image_2.setPixmap(pixmap)
        self.point_image_2.move(75 + (32+ 5), 190)
        self.point_image_2.show()
        self.point_image_3.setPixmap(pixmap)
        self.point_image_3.move(75 + 2 * (32+ 5), 190)
        self.point_image_3.show()

        self.point_image_4.setPixmap(pixmap)
        self.point_image_4.move(425, 190)
        self.point_image_4.show()
        self.point_image_5.setPixmap(pixmap)
        self.point_image_5.move(425 + (32 + 5), 190)
        self.point_image_5.show()
        self.point_image_6.setPixmap(pixmap)
        self.point_image_6.move(425 + 2 * (32+ 5), 190)
        self.point_image_6.show()
        
        self.display_image()
        self.show()

    def display_image(self):
        self.image1 = QLabel(self)
        self.image2 = QLabel(self)
        self.timer = QTimer(self)
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

    def showImageChoices(self):
        self.image1.clear()
        self.image2.clear()
        pixmap = QPixmap("images/" + self.images[self.image_index])
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
        self.image1.setPixmap(pixmap)
        self.image1.move(75, 250)
        self.image1.show()
        pixmap = QPixmap("images/" + self.images[self.image_index_computer])
        pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
        self.image2.setPixmap(pixmap)
        self.image2.move(475, 250)
        self.image2.show()
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.player1_input.setReadOnly(True)
            self.player2_input.setReadOnly(True)
        elif event.key() == Qt.Key_M:
            self.player1_input.setReadOnly(False)
            self.player2_input.setReadOnly(False)
        elif event.key() == Qt.Key_Space and self.winner == "":
            self.timer.start(300)
        elif event.key() in [Qt.Key_Escape, Qt.Key_Q, Qt.Key_S, Qt.Key_D]:
            self.timer.stop()
            # select random in between 0 and 2 included
            self.image_index = [Qt.Key_Q, Qt.Key_S, Qt.Key_D].index(event.key())
            self.image_index_computer = random.randint(0, 2)
            pcr_str = " ".join([self.images[i].split('.')[0] for i in range(3)])
            print(pcr_str)
            print(f"Key pressed:  {event.text()} {self.images[self.image_index].split('.')[0]}")
            print(f"Computer choice: {self.image_index_computer} {self.images[self.image_index_computer].split('.')[0]}")
            if event.key() in [Qt.Key_Escape, Qt.Key_Q, Qt.Key_S, Qt.Key_D]:
                # self.timer.disconnect()
                self.timer.stop()
                print(f"Quit loop !")
            self.displayResults()
            if self.winner_window is None:
                self.drawScores()
                self.showImageChoices()
                self.show()
        else:
            pass

    def displayResults(self):
        # Display the results of the game
        print(f"image_index: {self.image_index}")
        print(f"image_index_computer: {self.image_index_computer}")

        if self.image_index == self.image_index_computer:
            pass
        elif (self.image_index + 1) % 3 == self.image_index_computer:
            print(f" {self.player1_input.text()} wins")
            # write text in green color
            self.player1_score += 1

        else:
            print(f" {self.player2_input.text()} wins")
            # write text in red color
            self.player2_score += 1
        print(f"Player 1 score: {self.player1_score}")
        print(f"Player 2 score: {self.player2_score}")
        print("\n\n\n")
        if self.player1_score == 3 or self.player2_score == 3:
            if self.player1_score == 3:
                self.winner = self.player1_input.text()
                print(f" {self.player1_input.text()} wins the game")
            elif self.player2_score == 3:
                self.winner = self.player2_input.text()
                print(f" {self.player2_input.text()} wins the game")
            self.endGame()

    def endGame(self):
        print('New window')
        self.winner_window = results.WinnerWindow(self.winner)
        self.winner_window.show()
        self.close()


    def drawScores(self):
        # Update the scores of the players
        if self.player1_score > 0 or self.player2_score > 0:
            pixmap = QPixmap("images/point.png").scaled(32, 32, Qt.KeepAspectRatio)
        else: return
        if self.player1_score == 1:
            self.point_image_1.setPixmap(pixmap)
            self.point_image_1.move(75, 190)
            self.point_image_1.show()
        elif self.player1_score == 2:
            self.point_image_2.setPixmap(pixmap)
            self.point_image_2.move(75 + (32 + 5), 190)
            self.point_image_2.show()
        elif self.player1_score == 3:
            self.point_image_3.setPixmap(pixmap)
            self.point_image_3.move(75 + 2 * (32 + 5), 190)
            self.point_image_3.show()
        if self.player2_score == 1:
            self.point_image_4.setPixmap(pixmap)
            self.point_image_4.move(425, 190)
            self.point_image_4.show()
        elif self.player2_score == 2:
            self.point_image_5.setPixmap(pixmap)
            self.point_image_5.move(425 + (32 + 5), 190)
            self.point_image_5.show()
        elif self.player2_score == 3:
            self.point_image_6.setPixmap(pixmap)
            self.point_image_6.move(425 + 2 * (32 + 5), 190)
            self.point_image_6.show()
        
