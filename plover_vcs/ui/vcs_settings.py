from PyQt5.QtWidgets import QDialog

from plover_vcs.ui.vcs_settings_ui import Ui_VcsSettings


class VcsSettings(QDialog, Ui_VcsSettings):

    def __init__(self):
        super(VcsSettings, self).__init__()
        self.setupUi(self)
