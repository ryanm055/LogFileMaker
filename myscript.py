import tkinter as tk

import os
import datetime
import random

from enum import Enum

#TODO WHEN HOME:
# Make the application work as expected, make amount of files as requested.
# Make clear inputs and delete log files work.
# Make open folder for easy navigation.
# Oh and fix status. Make it work. 
# Make a shell file for a user to be able to run the program without terminal.

####################
# Global variables.
####################
class SubmissionStatus(Enum):
    UNDETERMINED = "Undetermined (Hasn't been run yet)."
    FAIL = "Failed."
    SUCCESS = "Sucess."
status_of_submission = SubmissionStatus.UNDETERMINED

##############################
# Application Logic functions.
##############################
def createLogFiles():
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
        num_files_to_make = int(num_files_input.get())

        if (not (os.path.isdir(filepath))):
            os.mkdir(filepath)

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
                
        status_of_submission = SubmissionStatus.SUCCESS
    except Exception as e:
        print(f"Error: {e}")
        status_of_submission = SubmissionStatus.FAIL

def deleteLogFiles():
    pass

#############################
# Application GUI functions.
#############################
def clearAndResetInputs():
    status_of_submission = SubmissionStatus.UNDETERMINED

############################
# Main application window.
############################
# Window properties.
root = tk.Tk()
root.title("Log File Maker for YUBlueprint BlackCreek DBMS Project.")
root.minsize(800, 500)

# Top message / title.
top_message_label = tk.Label(root, text="Log File Maker!", padx=20, pady=10, font=("Arial", 16, "bold"))
top_message_label.pack()

# Number of files to create.
num_files_label = tk.Label(root, text="How many files? (Each file is 1 MiB)")
num_files_input = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, variable=tk.IntVar(value=1))
num_files_label.pack()
num_files_input.pack()

# Warning message.
warning_label = tk.Label(root, text="WARNING: Log files will be made in a folder in same directory as python script.")
warning_label.pack(pady=5)

# Status box.
status_label = tk.Label(root, text=f"STATUS: {status_of_submission.value}")
status_label.pack(pady=5)

# Submit button.
submit_button = tk.Button(root, text="Submit", command=createLogFiles)
submit_button.pack(pady=5)

# Clear and reset inputs.
clear_inputs_button = tk.Button(root, text="Clear Inputs", command=clearAndResetInputs)
clear_inputs_button.pack()

# There should be an option to clear/delete all log files in a specified folder.
delete_log_files = tk.Button(root, text="Delete Log Files", command=deleteLogFiles)
delete_log_files.pack()

# Loop main event.
root.mainloop()


###############
# END.
###############