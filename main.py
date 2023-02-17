import sys 
from PyQt5.QtWidgets import QApplication

# from start import RockPaperScissorsWindow
import start

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = start.RockPaperScissorsWindow()
    window.show()
    sys.exit(app.exec_())