import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import serial
import threading


class ServoSlider(QWidget):
    def __init__(self, parent = None):
        super(ServoSlider, self).__init__(parent)
        layout = QVBoxLayout()

        self.sl = QSlider(Qt.Horizontal)
        self.sl.setMinimum(0)
        self.sl.setMaximum(180)
        self.sl.setValue(90)
        self.sl.setTickPosition(QSlider.TicksBelow)
        self.sl.setTickInterval(5)

        layout.addWidget(self.sl)
        self.sl.valueChanged.connect(self.value_change)
        self.setLayout(layout)
        self.setWindowTitle("Servo Controller")

        self.ser = serial.Serial('/dev/tty.usbmodem1411')
        thread = threading.Thread(target=self.read_from_serial, args=(self.ser, ))
        thread.start()

    def value_change(self):
        size = self.sl.value()
        self.ser.write(str(size) + "\n")

    def read_from_serial(self, ser):
        while True:
            print(ser.readline())

def main():
    app = QApplication(sys.argv)
    ex = ServoSlider()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()