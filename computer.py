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
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print("Adding {}".format(chosen_part))
    else:
        print("Please add options from the lists")
        #to print the menu
        for key, value in available_parts.items():
            print("{}: {}".format(key, value))
        print("0: to finish")

    current_choice = input("> ")