from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.cw = QWidget()
        self.vlayout = QVBoxLayout()
        self.cw.setLayout(self.vlayout)
        self.setCentralWidget(self.cw)

        # Titulo da janela
        self.setWindowTitle('Calculadora')


    # Tamanho da janela
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # Adiciona um widget a janela
    def addWidgetToVLayout(self, widget: QWidget):
        self.vlayout.addWidget(widget)
        self.adjustFixedSize()