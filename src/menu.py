import replit
from screens import print_centred
from input_validator import validate_country_input, valid_countries_names
from input_validator import validate_data_explorer_restart
from country import Country
from displaygraph import DisplayGraph


# function to print out graph menu options
def display_options():
    print_centred("What data would you like to explore for a country?\n")
    print_centred("1. 14 Day Average Cases      2. Cumulative Deaths        "
                  "3. Case Fatality Rates        4. Available Countries")


# function to prompt user if they want to continue exploring the data
def keep_exploring_prompt(data_explorer):

    print_centred("Keep exploring? (Y/N)")

    while True:
        try:
            data_explorer_restart = input("")
            if validate_data_explorer_restart(data_explorer_restart) is True:
                replit.clear()
                data_explorer = True
                return data_explorer

            elif validate_data_explorer_restart(
                    data_explorer_restart) is False:
                replit.clear()
                data_explorer = False
                return data_explorer

            else:
                print_centred("This is not a valid letter. "
                              "Please enter Y or N")

        except ValueError:
            print_centred("This is not a valid option. "
                          "Please enter a valid option (Y or N).")


# function for selection 1 of menu
def selection_one(data_explorer):

    # clear the screen
    replit.clear()

    # centre the screen
    print_centred("\n")

    # print prompt for user to type in country name or code
    print_centred("Type in a Country Name or Country Code")

    # error handling/try and except block for valid country,
    # to ensure API can be called properly.
    while True:
        country_fourteen_day_average_selection = input("")

        if validate_country_input(
                country_fourteen_day_average_selection) is True:
            break
        else:
            print_centred("This is not a valid country name. "
                          "Please enter in a valid country name")
            continue

    # instantiate country_fourteen_day_average object with Country class,
    # get_data instance method and parse data instance method
    country_fourteen_day_average = Country(
        country_fourteen_day_average_selection).get_data().parse_data()

    # clear the screen
    replit.clear()

    # centre the screen
    print_centred("\n")

    # initalise x_axis_days_data and y_axis_case_fatality_rate_data for
    # displaygraph, for animated graph
    x_axis_days_data = [0]
    y_axis_fourteen_day_average_cases = [0]

    # instantiate displaygraph object with DisplayGraph class
    displaygraph = DisplayGraph()

    # call displaygraph.display_fourteen_day_average_graph instance method
    # to display animated graph
    displaygraph.display_fourteen_day_average_graph(
        country_fourteen_day_average, x_axis_days_data,
        y_axis_fourteen_day_average_cases)

    # return keep_exploring_prompt(data_explorer) to continue or exit program
    return keep_exploring_prompt(data_explorer)


# function for selection 2 of menu
def selection_two(data_explorer):

    # clear the screen
    replit.clear()

    # centre the screen
    print_centred("\n")

    # print prompt for user to type in country name or code
    print_centred("Type in a Country Name or Country Code")

    # error handling/try and except block for valid country, to ensure
    # API can be called properly.
    while True:
        country_total_deaths_selection = input("")

        if validate_country_input(country_total_deaths_selection) is True:
            break
        else:
            print_centred("This is not a valid country name. "
                          "Please enter in a valid country name")
            continue

    # instantiate country_total_deaths object with Country class, get_data
    # instance method and parse data instance method
    country_total_deaths = Country(
        country_total_deaths_selection).get_data().parse_data()

    # clear the screen
    replit.clear()

    # centre the screen
    print_centred("\n")

    # initalise x_axis_days_data and y_axis_case_fatality_rate_data
    # for displaygraph, for animated graph
    x_axis_days_data = [0]
    y_axis_cummulative_deaths = [0]

    # instantiate displaygraph object with DisplayGraph class
    displaygraph = DisplayGraph()

    # call displaygraph.display_total_deaths instance method to display
    # animated graph
    displaygraph.display_total_deaths(
        country_total_deaths, x_axis_days_data, y_axis_cummulative_deaths)

    # return keep_exploring_prompt(data_explorer) to continue or exit program
    return keep_exploring_prompt(data_explorer)


# function for selection 3 of menu
def selection_three(data_explorer):

    # clear the screen
    replit.clear()

    # centre the screen
    print_centred("\n")

    # print prompt for user to type in country name or code
    print_centred("Type in a Country Name or Country Code")

    # error handling/try and except block for valid country, to ensure API
    # can be called properly.
    while True:
        country_case_fatality_rate_selection = input("")

        if validate_country_input(
                country_case_fatality_rate_selection) is True:
            break
        else:
            print_centred("This is not a valid country name. "
                          "Please enter in a valid country name")
            continue

    # instantiate country_case_fatality_rate object with Country class,
    # get_data instance method and parse data instance method
    country_case_fatality_rate = Country(
        country_case_fatality_rate_selection).get_data().parse_data()

    # clear the screen
    replit.clear()

    # centre the screen
    print_centred("\n")

    # initalise x_axis_days_data and y_axis_case_fatality_rate_data for
    # displaygraph, for animated graph
    x_axis_days_data = [0]
    y_axis_case_fatality_rate_data = [0]

    # instantiate displaygraph object with DisplayGraph class
    displaygraph = DisplayGraph()

    # call displaygraph.display_case_fatality_rate instance method to
    # display animated graph
    displaygraph.display_case_fatality_rate(
        country_case_fatality_rate, x_axis_days_data,
        y_axis_case_fatality_rate_data)

    # return keep_exploring_prompt(data_explorer) to continue or exit program
    return keep_exploring_prompt(data_explorer)


# function for selection 4 of menu
def selection_four(data_explorer):

    # prints available countries in the COVID19 API
    print(*valid_countries_names, sep='\n')

    return keep_exploring_prompt(data_explorer)
