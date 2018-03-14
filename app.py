# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
widget = QWidget()
widget.setWindowTitle('Hello World')
widget.show()
sys.exit(app.exec_())
