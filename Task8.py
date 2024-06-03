import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog


class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)

        self.btn = QPushButton('Select File', self)
        self.btn.setGeometry(100, 50, 100, 50)
        self.btn.clicked.connect(self.showDialog)

        self.setWindowTitle('File Converter')
        self.show()

    def showDialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if file_name:
            print(f"Selected file: {file_name}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ConverterApp()
    sys.exit(app.exec_())
