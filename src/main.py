# importing other python librarys
import sys

# importing pyside6 estensials
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QApplication, QLineEdit, QComboBox

# custom widget imports


# custom application module imports


# the main applicarion loop
class MainApplication(QApplication):
    def __init__(self):
        super().__init__()

        # loading our ui
        ui_file = QFile("src/Ui/Main.ui")
        if not ui_file.open(QFile.ReadOnly):
            # error has occured
            print(f"Oh noes! ;( looks like the file: {ui_file.fileName()}, could not be loaded because of error: {ui_file.errorString()}")
            sys.exit(-1)

        # using PySide6's ui loader
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        if not self.window:
            print(f"Failed to load UI: {loader.errorString()}")
            sys.exit(-1)

        # setting up window
        self.window.setFixedSize(650, 590)

        # getting widgets
        self.search_box = self.window.findChild(QLineEdit, "SearchBar")
        self.filter_box = self.window.findChild(QComboBox, "Filters")

        # setting up widgets and events
        filter_opitions = ["Installed", "Not Installed", "A-Z", "Z-A"]
        for fliter_op in filter_opitions:
            self.filter_box.addItem(fliter_op)
        self.filter_box.setCurrentIndex(1)
        self.search_box.editingFinished.connect(self.on_search_finished)

        # showing window
        self.window.show()

    def on_search_finished(self):
        print(self.search_box.text())


if __name__ == "__main__":
    app = MainApplication()
    sys.exit(app.exec())


        