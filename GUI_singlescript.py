import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPlainTextEdit, QLabel, QGridLayout, QPushButton, QWidget, QMessageBox
import script_checker


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sprawdzarka ")
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)        
        self.grid = QGridLayout()
        self.grid.setSpacing(10)
        self.wid.setLayout(self.grid)

        self.scriptfield = QPlainTextEdit()
        self.stdinfield = QPlainTextEdit()
        self.stdoutfield = QPlainTextEdit()
        self.checkbutton = QPushButton("Sprawdź!")

        self.grid.addWidget(QLabel("Kod skryptu:"), 0, 0)
        self.grid.addWidget(self.scriptfield, 1, 0, 3, 7)
        self.grid.addWidget(QLabel("Wejście:"), 5, 0)
        self.grid.addWidget(QLabel("Oczekiwane wyjście:"), 5, 4)
        self.grid.addWidget(self.stdinfield, 6, 0, 2, 3)
        self.grid.addWidget(self.checkbutton, 6, 3)
        self.grid.addWidget(self.stdoutfield, 6, 4, 2, 3)
        
        self.setLayout(self.grid)
        self.setGeometry(300,300,350,300)

        self.checkbutton.clicked.connect(self.check)

        self.show()

    def check(self):
        script = self.scriptfield.toPlainText()
        stdin = self.stdinfield.toPlainText()
        stdout = self.stdinfield.toPlainText()
        result = script_checker.test_script(['python', '-c', script], [stdin, stdout, '1'])
        messagestring = ''
        if result[1] == 1:
            messagestring = "Wynik skryptu zgadza się z oczekiwanym wynikiem!\n(czas wykonania: "+str(result[0])+")"
        elif result[2] == 1:
            messagestring = "Wynik skryptu różni się od oczekiwanego wyniku!\n(czas wykonania: "+str(result[0])+")"
        elif result[3] == 1:
            messagestring = "Wykonywanie skryptu zostało przerwane - timeout\n(czas wykonywania: "+str(result[0])+")"
        msg = QMessageBox.about(self, "Skrypt został przetestowany", messagestring)



app = QApplication(sys.argv)


window = Window()
window.show()
sys.exit(app.exec_())