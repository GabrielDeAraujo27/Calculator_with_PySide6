import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from main_window import MainWindow
from styles import setupTheme
from info import Info
from display import Display
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()

    window = MainWindow()

    label1 = QLabel('Calculadora')
    label1.setStyleSheet('font-size: 150px;')
    window.addWidgetToVLayout(label1)

    # Define o icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)
    #window.addWidgetToVLayout(Display('3'))
    #window.addWidgetToVLayout(Display('4'))


    window.show()
    app.exec()