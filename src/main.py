# importing other python librarys
import sys, platform

# importing pyside6 estensials
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt
from PySide6.QtWidgets import QApplication, QLineEdit, QComboBox, QPushButton, QScrollArea, QVBoxLayout, QWidget, QMessageBox

# custom widget imports
from Widgets.package_card import PackageCard

# custom application module imports
from libs import pip_manager

# the main applicarion loop
class MainApplication(QApplication):
    def __init__(self):
        super().__init__()

        # loading our ui
        match platform.system():
            case "Windows":
              ui_file = QFile("Ui\\Main.ui")
            case "Linux":
              ui_file = QFile("Ui/Main.ui")  
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
        self.window.setFixedSize(674, 686)

        # getting widgets
        self.search_box = self.window.findChild(QLineEdit, "SearchBar")
        self.filter_box = self.window.findChild(QComboBox, "Filters")
        self.find_btn = self.window.findChild(QPushButton, "FindButton")
        self.scroll_area = self.window.findChild(QScrollArea, "DescriptionFrame")

        # setting up widgets and events
        filter_opitions = ["Installed", "Not Installed", "A-Z", "Z-A"]
        for fliter_op in filter_opitions:
            self.filter_box.addItem(fliter_op)
        self.filter_box.setCurrentIndex(1)
        self.search_box.editingFinished.connect(self.on_search_finished)
        self.find_btn.pressed.connect(self.on_search_finished)

        # Create the widget that will live inside the scroll area
        self.scroll_container = QWidget()

        # Create a vertical layout
        self.scroll_layout = QVBoxLayout(self.scroll_container)

        # Optional
        self.scroll_layout.setSpacing(10)
        self.scroll_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll_layout.setContentsMargins(10, 10, 10, 10)

        # Tell the scroll area to use it
        self.scroll_area.setWidget(self.scroll_container)
        self.scroll_area.setWidgetResizable(True)

        # showing window
        self.window.show()

    def on_search_finished(self):
        if self.search_box.text() != "":
            print(self.search_box.text())
            new_card = PackageCard()
            package_information = pip_manager.get_package_information(self.search_box.text())
            # checking to make sure we are not getting an error string, but a tuple value
            if type(package_information) != str:
                new_card.set_name(package_information[0])
                new_card.set_versions()
            #new_card.set_description("Test")
            #new_card.set_name("package")
            #new_card.set_versions(["1", "2", "3", "4"])
            self.scroll_layout.addWidget(new_card)


if __name__ == "__main__":
    app = MainApplication()
    sys.exit(app.exec())


        
