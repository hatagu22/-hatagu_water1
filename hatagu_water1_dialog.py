from PyQt5 import QtWidgets
from .hatagu_water1_dialog_base import Ui_HataguWater1DialogBase

class HataguWater1Dialog(QtWidgets.QDialog, Ui_HataguWater1DialogBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)