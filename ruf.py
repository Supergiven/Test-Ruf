from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
app = QApplication([])

win = QWidget()
win.setWindowTitle('Тест Руфье')
win.move(700, 500)
win.show()

app.exec_()