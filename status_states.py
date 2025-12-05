from enum import Enum

class statusStates(Enum):
    UNDETERMINED = "Undetermined."
    CREATION_SUCESS = "Creation of log files was successful."
    CREATION_FAILED = "Creation of log files failed."
    DELETION_SUCESS = "Deletion of log files was successful."
    DELETION_FAILED = "Deletion of log files failed."
    DELETION_NOT_HAPPENED = "No deletion has occurred as there is no 'logfiles' folder."
    INVALID_INPUT = "User input was invalid."
    RESET = "Application has been reset to initial state."
