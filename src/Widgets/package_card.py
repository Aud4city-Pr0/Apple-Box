# other python modules
import sys

# importing pyside files
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QWidget, QLabel, QComboBox, QSizePolicy

# the package card class
class PackageCard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.package_name = ""
        self.versions = []

        # loading ui
        ui_file = QFile("Ui/PackageCard.ui")
        if not ui_file.open(QFile.ReadOnly):
            # error has occured
            print(f"Oh noes! ;( looks like the file: {ui_file.fileName()}, could not be loaded because of error: {ui_file.errorString()}")
            sys.exit(-1)
        
        # using PySide6's ui loader
        loader = QUiLoader()
        loader.load(ui_file, self)
        ui_file.close()

        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )
        self.setFixedHeight(250)

        # getting important components like, name, description, and version widgets
        self.name_lable = self.findChild(QLabel, "Name")
        self.description_lable = self.findChild(QLabel, "Description")
        self.versions_box = self.findChild(QComboBox, "VersionsBox")

    def set_name(self, name):
        self.package_name = name
        self.name_lable.setText(self.package_name)

    def set_description(self, desc):
        self.description_lable.setText(desc)

    def set_versions(self, vers):
        self.versions = vers
        for ver in self.versions:
            print(f"Version: {ver}")
            self.versions_box.addItem("Version: " + ver)

    