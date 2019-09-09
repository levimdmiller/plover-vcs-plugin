from PyQt5.QtWidgets import QDialog, QFileDialog

from plover_vcs.ui.vcs_settings_ui import Ui_VcsSettings


class VcsSettings(QDialog, Ui_VcsSettings):

    def __init__(self):
        super(VcsSettings, self).__init__()
        self.setupUi(self)
        self.addDictionaryButton.clicked.connect(self.add_dictionary)
        self.removeDictionaryButton.clicked.connect(self.remove_dictionary)
        self.dictionariesListWidget.itemDoubleClicked.connect(self.edit_dictionary)

    def add_dictionary(self):
        self.dictionariesListWidget.addItem('<dictionary>')

    def remove_dictionary(self):
        for item in self.dictionariesListWidget.selectedItems():
            self.dictionariesListWidget.takeItem(self.dictionariesListWidget.row(item))

    def edit_dictionary(self, item):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Dictionary File", "", "JSON Files (*.json)")
        if file_name:
            item.setText(file_name)
