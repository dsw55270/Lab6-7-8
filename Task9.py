import threading

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.btn = QPushButton('Select File', self)
        self.btn.clicked.connect(self.showDialog)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.setWindowTitle('File Converter')
        self.show()

    def showDialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if file_name:
            threading.Thread(target=self.processFile, args=(file_name,)).start()

    def processFile(self, file_name):
        print(f"Processing file: {file_name}")

app = QApplication(sys.argv)
ex = ConverterApp()
sys.exit(app.exec_())
