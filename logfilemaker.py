import sys
import os
import datetime
import random

from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLabel,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget
)
from PySide6.QtCore import Qt

############################################################################
## DEV NOTES FOR LATER:
## 1. Make clear inputs and delete log files button.
## 2. Make open folder / being able to choose where the log files made go.
## 3. Add status, to let user know that job was successful or not (Use Enum).
## 4. Make a shell file that user opens to run the program, without having to install python and use terminal to run it.
## 5. Fix styling, make it look better overall.
############################################################################

################
## Main window.
################
class MainWindow(QMainWindow):
    """
    Customizing main window of application.
    """
    def __init__(self):
        super().__init__()

        ### Style Variables.
        title_text_styling = "font-weight: bold; font-size: 24px; margin: 0px;"
        default_text_styling = "font-size: 16px; margin: 0px;"
        submit_button_styling = "font-size: 16px;"

        ### Window.
        self.setWindowTitle("Log File Maker for YU Blueprint BlackCreek DBMS Project")
        self.setFixedSize(800, 500)

        ### Title of application.
        title_label = QLabel("Log File Maker!")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet(title_text_styling)

        ### Number of files.
        # Label.
        num_of_files_label = QLabel("How many files? (Each file is 1 MB)")
        num_of_files_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        num_of_files_label.setStyleSheet(default_text_styling)
        # Display current value on slider.
        self.slider_label = QLabel("Current Value: 1")
        self.slider_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.slider_label.setStyleSheet(default_text_styling)
        # Number range/slider.
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(1, 10)
        self.slider.setValue(1)

        ### Buttons.
        # Clear inputs.
        # Delete log files.

        ### Submit button.
        self.submit_button = QPushButton("Submit.")
        self.submit_button.setStyleSheet(submit_button_styling)

        ### Container.
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        ### Layout.
        layout.addWidget(title_label)
        layout.addWidget(num_of_files_label)
        layout.addWidget(self.slider_label)
        layout.addWidget(self.slider)
        layout.addWidget(self.submit_button)
        self.setCentralWidget(container)

        ### Updating values.
        # Slider update.
        self.slider.valueChanged.connect(self.update_label)
        # Submit button update.
        self.submit_button.clicked.connect(self.button_clicked)

    #######################################
    ## Application logic functions.
    #######################################
    def update_label(self, value):
        """
        Update the current value label for slider. Updates every time slider moves.
        """
        self.slider_label.setText(f"Current Value: {value}")

    def button_clicked(self):
        """
        Creates log files based on user input.
        """
        # Size of each file and count.
        count = 1
        num_of_mb = 1
        num_of_bytes = num_of_mb * (1024 * 1024)

        # Names to randomly select from.
        users = ['ryan', 'souplover123', 'YayLol', 'Tamara', 'Daniel', 'Garfield', 'Odie', 'John', 'Albert', 'Arnold', 'Anthony', 'George', 'Bill', 'Richard', 'Grimdale', 'Zywoo', 'N1k0', 'Iona', 'Lachlan', 'Lillian', 'Kevin', 'abc123', 'Pierre', 'Mark', 'David', 'ropz']
        actions = ['added', 'deleted', 'edited']
        fields = ['equipment', 'livestock', 'supply', 'crop']

        # Adjectives for fields.
        adjectives = ["Test", "Sample", "Prototype", "Some", "Type Of", "Interesting", "Cool", "Hard", "Strong", "Light"]

        # File name and paths.
        filepath = f"logfiles/"
        filename = f"modification_activites_{count}.log"
        full_filename = filepath + filename

        try:
            num_files_to_make = int(self.slider.value())

            if (not (os.path.isdir(filepath))):
                os.mkdir(filepath)

            while count <= num_files_to_make:
                with open(full_filename, "w") as f:
                    while (os.path.getsize(full_filename) < num_of_bytes):
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        user = random.choice(users)
                        action = random.choice(actions)
                        field = random.choice(fields)
                        adjective = random.choice(adjectives)
                        random_number = random.randint(1, 10000)

                        name_of_object = f"{adjective} {field.capitalize()} {random_number}"
                        message = f"User {user} {action} {field}: {name_of_object}"

                        line_to_make = f"[{timestamp}] {message}\n" 

                        # Format of each line:[2025-11-02 18:02:54] User ryan deleted supply: Test Supply A
                        f.write(line_to_make)
                count = count + 1
                filename = f"modification_activites_{count}.log"
                full_filename = filepath + filename

        except Exception as e:
            print(f"Error: {e}")

def run_app():
    """
    Running PySide application.
    """
    app = QApplication(sys.argv) 

    window = MainWindow()
    window.show()

    sys.exit(app.exec()) 

if __name__ == "__main__":
    run_app()