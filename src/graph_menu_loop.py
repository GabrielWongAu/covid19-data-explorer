import os

from screens import print_centred
from menu import (
    display_options, selection_one,
    selection_two, selection_three, selection_four)

from input_validator import validate_menu_selection

TERMX, TERMY = os.get_terminal_size()


# graph_menu_loop function to display graphs menu
def graph_menu_loop():
    # set data_explorer to true for the while loop
    data_explorer = True

    while data_explorer is True:

        # centre screen
        print_centred("\n" * ((TERMY - 11) // 2))

        # function to print out menu options
        display_options()

        # error handling/try and except block for menu selection
        while True:
            try:
                selection = input("".center(TERMX // 2))

                # method to validate menu selection
                if validate_menu_selection(selection) is False:
                    print_centred(
                        "This is not a valid number. "
                        "Please enter a valid number.")
                else:
                    break
            except ValueError:
                print_centred(
                    "This is not a valid number. Please enter a valid number.")
            except TypeError:
                print_centred(
                    "This is not a valid number. Please enter a valid number.")

        # if selection 1 is chosed, call selection_one function.
        if selection == "1":
            if selection_one(data_explorer) is False:
                data_explorer = False
                break
            else:
                continue

        # if selection 2 is chosed, call selection_two function.
        elif selection == "2":
            if selection_two(data_explorer) is False:
                data_explorer = False
                break
            else:
                continue

        # if selection 3 is chosed, call selection_three function.
        elif selection == "3":
            if selection_three(data_explorer) is False:
                data_explorer = False
                break
            else:
                continue

        # if selection 4 is chosed, call selection_four function.
        elif selection == "4":
            if selection_four(data_explorer) is False:
                data_explorer = False
                break
            else:
                continue
