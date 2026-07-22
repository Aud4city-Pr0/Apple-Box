# importing other python librarys
import sys

# importing pyside6 estensials
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtWidgets import QApplication

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

        # showing window
        self.window.show()


if __name__ == "__main__":
    app = MainApplication()
    sys.exit(app.exec())


        