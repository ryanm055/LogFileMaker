# Log File Maker
## Purpose
This tool was made for the YU Blueprint BlackCreek DBMS project. It creates sample modification activities log files to test all sorts of cases when it comes to any part of the application that uses them (retrieving activities, etc). It generates a specified number of 1 MB files with each line being in the activity logging format.

## How to run
For now, have python downloaded and type 'python3 logfilemaker.py' in the directory where the python script is located. Might install need to pip install PySide6.

## BlackCreek DBMS Project
[BlackCreek DBMS Project](https://github.com/yublueprint/BlackCreekFarm)

## Other
N/A

# DEV NOTES / THINGS TO IMPLEMENT LATER
* Fix Frontend.
    * Make sure the screen sized is fixed and permanent (not possible to expand or open full window).
    * Think of a better dark coloured theme. Go to UIVerse and see the dark coloured theme components / forms. Actually do light coloured, make it similar to the blackcreek dbms colours. This includes making the font 'Open Sans'.
    * Have shadows.
    * Each section would have its own background hovering over them main background, using shadows to make that illusion.
    * Make status update whether the submit button worked or not. Make sure the submit button has 5 second cooldown to prevent spam.
    * Make warning text be black and back ground color yellow. Maybe include the title description with it too.
    * Make it possible to choose where log files go.
    * Make all buttons (clear and delete) functional.
* Once completely finished, make program compiled into executable that can run on any desktop platform (Windows, MacOS, Linux, etc).