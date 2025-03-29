import sys
from PyQt5 import QtWidgets, uic
from canvas import Canvas

class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

        self.t0Edit = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.tenvEdit = self.findChild(QtWidgets.QLineEdit, "lineEdit_2")
        self.kEdit = self.findChild(QtWidgets.QLineEdit, "lineEdit_3")
        self.btn = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.canvasWidget = self.findChild(QtWidgets.QWidget, "widget")

        self.canvas = Canvas(self.canvasWidget)
        layout = QtWidgets.QVBoxLayout(self.canvasWidget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)

        self.btn.clicked.connect(self.doPlot)

    def doPlot(self):
        try:
            T0 = float(self.t0Edit.text())
            Tenv = float(self.tenvEdit.text())
            k = float(self.kEdit.text())
            self.canvas.plot_temp(T0, Tenv, k)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "ошибка", "введите число")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWin()
    win.resize(800, 800)
    win.show()
    sys.exit(app.exec_())
