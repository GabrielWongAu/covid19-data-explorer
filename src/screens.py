import sys
import os

#function to centre text
def print_centred(line):

    TERMX, TERMY = os.get_terminal_size()
    print(*centred(line))

#helper function of print_centered to centre text
def centred(*lines):

    TERMX, TERMY = os.get_terminal_size()
    for line in lines:
        yield line.center(TERMX)                                                                                             


#prints out introduction screen information
def intro_screen():

    TERMX, TERMY = os.get_terminal_size()
    print_centred("\n" * ((TERMY - 6 - 5) // 2)) 
    print_centred(" ██████  ██████  ██    ██ ██ ██████   ██  █████      ██████   █████  ████████  █████      ███████ ██   ██ ██████  ██       ██████  ██████  ███████ ██████  ")
    print_centred("██      ██    ██ ██    ██ ██ ██   ██ ███ ██   ██     ██   ██ ██   ██    ██    ██   ██     ██       ██ ██  ██   ██ ██      ██    ██ ██   ██ ██      ██   ██ ")
    print_centred("██      ██    ██ ██    ██ ██ ██   ██  ██  ██████     ██   ██ ███████    ██    ███████     █████     ███   ██████  ██      ██    ██ ██████  █████   ██████  ")
    print_centred("██      ██    ██  ██  ██  ██ ██   ██  ██      ██     ██   ██ ██   ██    ██    ██   ██     ██       ██ ██  ██      ██      ██    ██ ██   ██ ██      ██   ██ ")
    print_centred(" ██████  ██████    ████   ██ ██████   ██  █████      ██████  ██   ██    ██    ██   ██     ███████ ██   ██ ██      ███████  ██████  ██   ██ ███████ ██   ██ ")
    print_centred("                                                                                                                                                           ")
    print_centred("Developed by Gabriel Wong")
    print_centred("")
    print_centred("Welcome to the COVID19 Data Explorer: a visualisation tool to explore the latest current COVID19 dataset.")
    print_centred("") 
    print_centred("Application Description: Explore a country's 14 day case average, cumulative deaths and case fatality rate, via an animated graph.")
    print_centred("API Data Source: covid19api.com created by Kyle Redelinghuys. This API takes its data from Johns Hopkins CSSE.")
    print_centred("")
    print_centred("Public Saftey Announcement: Saves lives by wearing a mask. Limit face-to face contact and stay at home.\n")
    print_centred("")
    print_centred("Press Enter to continue")
    new = input(("").center(TERMX // 2))
    os.system('clear')

#prints out ending screen message
def ending_screen():
    TERMX, TERMY = os.get_terminal_size()
    print_centred("\n" * ((TERMY - 6 - 5) // 2)) 
    print_centred("Thank you for using COVID19 Data Explorer\n")
    print_centred("Made with <3")
    print_centred("\n" * ((TERMY - 6 - 5) // 2)) 
