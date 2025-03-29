import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Canvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(figsize=(6, 4), dpi=100)
        super().__init__(self.fig)
        self.setParent(parent)

        self.ax.set_xlabel("Время (с)")
        self.ax.set_ylabel("Температура (°C)")
        self.ax.grid(True)

    def plot_temp(self, T0, Tenv, k):
        self.ax.clear()
        self.ax.set_xlabel("Время (с)")
        self.ax.set_ylabel("Температура (°C)")
        self.ax.grid(True)

        t = np.linspace(0, 300, 500)
        temp = Tenv + (T0 - Tenv) * np.exp(-k * t)

        self.ax.plot(t, temp)
        self.draw()
