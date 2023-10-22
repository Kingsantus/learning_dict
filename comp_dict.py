available_parts = {
    '1': 'CPU',
    '2': 'Keyboard',
    '3': 'Mouse',
    '4': 'Monitor',
    '5': 'DVD drive',
    '6': 'HDMI cable',
    '7': 'WIFI adapter',
    '8': 'Bluetooth adapter'
}

#getting a user choice
current_choice = None
computer_parts = [] # create an empty list

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:
            #it's already in, so remove it
            print("Removing {}".format(chosen_part))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(chosen_part))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the lists")
        #to print the menu
        for key, value in available_parts.items():
            print("{}: {}".format(key, value))
        print("0: to finish")

    current_choice = input("> ")