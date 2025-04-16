from PySide6 import QtWidgets, QtGui

class RCFToolbar(QtWidgets.QToolBar):
    def __init__(self, api):
        super(RCFToolbar, self).__init__(parent=api.main_window)

        self.setObjectName('RCFToolbar')
        self.API = api