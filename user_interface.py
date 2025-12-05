import sys
import os
import datetime
import random

from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader

from status_states import statusStates

loader = QUiLoader()

class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("LogFileMakerUI.ui", None)
        self.ui.setWindowTitle("LogFileMaker for YU Blueprint BlackCreek DBMS Project")
        self.ui.numFilesSlider.valueChanged.connect(self.update_slider_val_label)
        self.ui.submit_button.clicked.connect(self.submit_button_clicked)
        self.ui.clearInputsBtn.clicked.connect(self.reset_user_inputs)
        self.ui.deleteLogFilesBtn.clicked.connect(self.delete_button_clicked)
    def show(self):
        self.ui.show()

    #######################################
    ## Application logic functions.
    #######################################
    def update_slider_val_label(self, value):
        """
        Update the current value label for slider. Updates every time slider moves.
        """
        self.ui.numFilesCurValLabel.setText(f"Current value: {value}")

    def update_status_state_label(self, value):
        """
        Update the status state label based on current status state.
        """
        print(f"STATUS: {value}")
        self.ui.statusValueLabel.setText(f"{value}")
    
    def submit_button_clicked(self):
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
        filename = f"modification_activities_{count}.log"
        full_filename = filepath + filename

        try:
            num_files_to_make = int(self.ui.numFilesSlider.value())

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
                filename = f"modification_activities_{count}.log"
                full_filename = filepath + filename
                self.update_status_state_label(statusStates.CREATION_SUCESS.value)

        except Exception as e:
            print(f"Error: {e}")
            self.update_status_state_label(statusStates.CREATION_FAILED.value)

    def delete_button_clicked(self):
        try:
            if (os.path.isdir("logfiles/")):
                for file in os.listdir("logfiles/"):
                    if f"modification_activities" in file:
                        file_path = os.path.join("logfiles/", file)
                        if os.path.isfile(file_path):
                            print(f"It got to {file_path}")
                            os.remove(file_path)
                # os.rmdir("logfiles/")
            else:
                self.update_status_state_label(statusStates.DELETION_NOT_HAPPENED.value)
                return
            self.update_status_state_label(statusStates.DELETION_SUCESS.value)
        except Exception as e:
            print(f"Error: {e}")
            self.update_status_state_label(statusStates.DELETION_FAILED.value)
            return

    def reset_user_inputs(self):
        """
        Resets all user inputs to default values and makes application go back to beginning state.
        """
        self.update_status_state_label(statusStates.RESET.value)
        self.ui.numFilesSlider.setValue(1)