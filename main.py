import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QVBoxLayout, QGridLayout, \
    QFormLayout, QLineEdit, QPushButton, QGroupBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from header import *

class LogoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.showMaximized()

        # Header
        self.MainLayout = QGridLayout()
        self.setLayout(self.MainLayout)

        self.h_label = QLabel("TSL", self)
        self.h_label.setStyleSheet("border: 2px solid black; color: white; background-color: blue; font-size: 50px;")
        self.h_label.setAlignment(Qt.AlignCenter)
        self.MainLayout.addWidget(self.h_label, 0, 0, 2, 27)

        # Logo
        self.label = QLabel(self)
        self.pixmap = QPixmap('image.png')
        self.label.setPixmap(self.pixmap)

        # Buttons
        self.modelbutton = QPushButton("Model", self)
        self.MainLayout.addWidget(self.modelbutton, 2, 1, 3, 3)

        self.graphbutton = QPushButton("Graph", self)
        self.MainLayout.addWidget(self.graphbutton, 4, 1, 2, 3 )

        self.drawbutton = QPushButton("Draw", self)
        self.MainLayout.addWidget(self.drawbutton, 6, 1, 2, 3 )

        self.pptbutton = QPushButton("PPT/Document",self)
        self.MainLayout.addWidget(self.pptbutton, 2, 23, 3, 3)

        self.optionsbutton = QPushButton("Options",self)
        self.MainLayout.addWidget(self.optionsbutton, 4,23,2,3)

        # Graph
        self.graphWidget1 = plt.figure()
        self.canvas = FigureCanvas(self.graphWidget1)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.graphWidget = QWidget()
        self.graph1Layout = QVBoxLayout(self.graphWidget)
        self.graph1Layout.setSpacing(0)
        self.graph1Layout.addWidget(self.toolbar)
        self.graph1Layout.addWidget(self.canvas)
        self.graph1Layout.setAlignment(Qt.AlignCenter)
        self.MainLayout.addWidget(self.graphWidget, 1, 5, 8, 17)

        # Input
        self.inputLayout = QFormLayout()

        self.userinput = QLabel("User Input", self)
        self.userinput.setStyleSheet("font-size: 20px; color: blue; border: 2px solid black;")
        self.inputLayout.addRow(self.userinput)

        self.input1_edit = QLineEdit()
        self.inputLayout.addRow("Input 1:", self.input1_edit)

        self.input2_edit = QLineEdit()
        self.inputLayout.addRow("Input 2:", self.input2_edit)

        self.input3_edit = QLineEdit()
        self.inputLayout.addRow("Input 3:", self.input3_edit)

        self.MainLayout.addLayout(self.inputLayout, 10, 5, 2, 6)

        # Output
        self.outputLayout = QFormLayout()

        self.useroutput = QLabel("Output", self)
        self.useroutput.setStyleSheet("font-size: 20px; color: blue; border: 2px solid black;")
        self.outputLayout.addRow(self.useroutput)

        self.output1_edit = QLineEdit()
        self.outputLayout.addRow("Output 1:", self.output1_edit)

        self.output2_edit = QLineEdit()
        self.outputLayout.addRow("Output 2:", self.output2_edit)

        self.output3_edit = QLineEdit()
        self.outputLayout.addRow("Output 3:", self.output3_edit)

        self.MainLayout.addLayout(self.outputLayout, 10, 15, 2, 5)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LogoWindow()
    window.show()
    sys.exit(app.exec_())
