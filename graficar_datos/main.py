import sys
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear datos para la animación
        self.x = np.linspace(0, 10, 100)
        self.phase = 0

        # Configurar la ventana
        self.setWindowTitle("Animación con PyQtGraph")
        self.setGeometry(100, 100, 800, 600)

        # Crear un widget de gráfico
        self.plot_widget = pg.PlotWidget(self)
        self.plot_widget.setGeometry(50, 50, 700, 500)
        self.setCentralWidget(self.plot_widget)

        # Configurar el eje x
        self.plot_widget.setLabel('bottom', 'Tiempo', units='s')

        # Configurar el eje y
        self.plot_widget.setLabel('left', 'Valor')

        # Inicializar la línea del gráfico
        self.curve = self.plot_widget.plot([], pen='r')

        # Iniciar la animación
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(50)  # Actualiza cada 50 milisegundos

    def update_plot(self):
        # Actualizar la fase de la función seno
        self.phase += 0.1

        # Calcular los valores de la función seno
        y = np.sin(self.x + self.phase)

        # Actualizar los datos del gráfico
        self.curve.setData(self.x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
