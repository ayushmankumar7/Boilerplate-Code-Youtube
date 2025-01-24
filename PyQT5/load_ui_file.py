""" 
Boilerplate Code by @ayushmankumar7 
Youtube Channel : Code to Win

    LOAD ANY .ui FILE DEVELOPED IN QT DESIGNER

"""

from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Ui, self).__init__(*args, **kwargs)
        uic.loadUi('example.ui', self) # Replace with your UI file
        self.show()
    
app = QtWidgets.QApplication([])
window = Ui()
app.exec_()