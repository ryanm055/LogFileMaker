import os
import datetime
import random

#Note:
# Ignore comments, just personal notes to self lol. 
# Count should be set to amount that doesn't exist.
# If modifcation_activties_1 and modifcation_activties_2 exist,
# then it should make modification_activities_3 and do stuff there.
# It uses random names, types of stuff for everything/ every field.

# User should be able to give the following inputs...
# Count: where to start, default start at 1 or 5. Maybe we should just make it rotate where the new file is always modification_activities and then rest are old versions like modification_activites_1 is made then new modification_activities is made. Idk if I should make it rotate. 
# Num of Megabytes: 1MB by default. 1024 * 1024 bytes.

count = 1
# honeslty should give options such as kb, mb, gb, then that's it.  1 for kb, 2 for mb, 3 for gb, else reprompt.
num_of_mb = 1
num_of_bytes = num_of_mb * (1024 * 1024)

# Names to randomly select from.
users = ['ryan', 'souplover123', 'YayLol', 'Tamara', 'Daniel', 'Garfield', 'Odie', 'John', 'Albert', 'Arnold', 'Anthony', 'George', 'Bill', 'Richard', 'Grimdale', 'Zyw00', 'N1k0', 'Iona', 'Lachlan', 'Lillian', 'Kevin', 'abc123', 'Pierre', 'Mark', 'David']
actions = ['added', 'deleted', 'edited']
fields = ['equipment', 'livestock', 'supply', 'crop']

# For Generating Names
adjectives = ["Test", "Sample", "Prototype", "Some", "Type Of", "Interesting", "Cool", "Hard", "Strong", "Light"]

filename = f"logfiles/modification_activites_{count}.log"

# Format of each line:[2025-11-02 18:02:54] User ryan deleted supply: Test Supply A
with open(filename, "w") as f:

    while (os.path.getsize(filename) < (num_of_bytes)):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user = random.choice(users)
        action = random.choice(actions)
        field = random.choice(fields)
        adjective = random.choice(adjectives)
        random_number = random.randint(1, 10000)

        name_of_object = f"{adjective} {field.capitalize()} {random_number}"
        message = f"User {user} {action} {field}: {name_of_object}"

        line_to_make = f"[{timestamp}] {message}\n" 

        f.write(line_to_make)

        #file_size = os.path.getsize(filename)
        #print(file_size)
