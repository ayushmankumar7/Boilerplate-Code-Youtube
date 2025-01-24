""" 
Boilerplate Code by @ayushmankumar7 
Youtube Channel : Code to Win

    Write an efficient thead using PyQT5

"""

from PyQt5.QtCore import QThread, pyqtSignal, Qt

class SampleThread(QThread):
    message_to_be_sent = pyqtSignal(str, int)  # Here we specify the list of Datatypes to be sent

    def run(self):
        while True:
            message1 = "hello"
            message2 = 69
            self.message_to_be_sent.emit(message1, message2) # Messages to be emitted in the same format as mentioned in line 12


class SampleUIFile:
    """ 
        This is a sample UI file 
        Notice: Here I am not loading any UI 
        This is just to showcase how you can use the above thread on your Application. 
        You may try it yourself by applying the same in 
        https://github.com/ayushmankumar7/Boilerplate-Code-Youtube/blob/master/PyQT5/load_ui_file.py
    """

    def __init__(self):
        self.myThread = SampleThread() 
        self.myThread.message_to_be_sent.connect(self.actiononThread) # This send the thread output directly to the passed function

    def actionOnThread(self, mymessage, number):
        """ 
            This function has the same type of Arguments as in the Thread output. 
            Data directly comes here for further processing according to need. 
            Data passed here through line 32
        """
        print(mymessage, number)