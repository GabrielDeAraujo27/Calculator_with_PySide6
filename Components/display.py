from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit
from Components import variables


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {variables.BIG_FONT_SIZE}px;')
        self.setMinimumHeight(variables.BIG_FONT_SIZE * 2.5)
        self.setMinimumWidth(variables.MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*(variables.TEXT_MARGIN for c in range(4)))