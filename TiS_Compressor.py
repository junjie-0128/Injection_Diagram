import sys
import PyQt5
import os
import json
from PyQt5.uic import loadUi
from os import path
from qtpy import QtCore
from pydm import Display
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QDoubleValidator, QValidator
from pydm.widgets import PyDMEmbeddedDisplay
from pydm.utilities import connection
from ophyd import EpicsSignal, EpicsSignalRO


class TiS_Compressor(Display):
    def __init__(self, parent=None, args=None, macros=None):
        super(TiS_Compressor, self).__init__(parent=parent, args=args, macros=macros)
        #self.ui.MP1_MR1_SHG_THG.clicked.connect(self.gotoMP1_MR1_SHG_THG)

        #self.ui.embeddedControl_MP1_MR1.embedded_widget.tip_mm.clicked.connect(self.tip11mm)

        #self.MP1_SPO1_pos = EpicsSignal('LM1K4:HRM_MP1_SPO1.DRBV', write_pv = "LM1K4:HRM_MP1_SPO1.VAL", name = 'MP1_SPO1_pos')

        #self.ui.MP1_MR1_tip_step_size = EpicsSignalRO('LM1K4:HRM_MP1_MR1_TIP1:STEP_COUNT', name = 'MP1_MR1_tip_step_size')

        #self.ui.MP1_MR1_tip_total_step = EpicsSignal('LM1K4:HRM_MP1_MR1_TIP1:TOTAL_STEP_COUNT', write_pv = "LM1K4:HRM_MP1_MR1_TIP1:SET_TOTAL_STEP_COUNT", name = 'MP1_MR1_tip_steps')

    def ui_filename(self):
        return "TiS_Compressor.ui"

    def ui_filepath(self):
        return path.join(path.dirname(path.realpath(__file__)), self.ui_filename())
    
    
#main
app = QApplication(sys.argv)
Compressor = TiS_Compressor()
widget = QtWidgets.QStackedWidget()
widget.addWidget(Compressor)
widget.setFixedHeight(700)
widget.setFixedWidth(1300)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("exiting")
