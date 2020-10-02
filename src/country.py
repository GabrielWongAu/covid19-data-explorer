import requests
import json
from screens import print_centred
import replit


# country class to instantiate country objects
class Country:
    def __init__(self, name: str):
        self.name = name

    # parse data instance method
    def parse_data(self) -> None:
        self.get_daily_cases()
        self.get_daily_deaths()
        self.get_cumulative_deaths()
        self.get_cumulative_cases()
        self.get_fourteen_day_average_cases()
        self.get_case_fatality_rate()
        self.get_graph_name(self.name)

        return self

    # get data method
    def get_data(self) -> None:

        from graph_menu_loop import graph_menu_loop

        # error handling/try and except block for when there is a requests
        # connectionError (i.e. no internet)
        error_handler_loop = True
        while error_handler_loop is True:
            try:
                # using Python Request, send a get request to the
                # specified URL
                response = requests.get(f"https://api.covid19api.com/total/dayone/country/{self.name}")
                break
            except requests.ConnectionError:

                # clear screen
                replit.clear()

                # centre screen
                print_centred("\n")
                print_centred("")

                # print error message
                print_centred(
                    "Unable to connect to https://api.covid19api.com/total/"
                    f"dayone/country/{self.name}\n")
                print_centred(
                    "Requests Connection Error -> Check Internet Connection\n")
                print_centred("Press Enter to continue")
                input("")

                # clear screen
                replit.clear()

                # set error_handler_loop to false to return back to menu
                error_handler_loop = False

        # if error_handler_loop is false, return back to menu selection.
        if error_handler_loop is False:
            graph_menu_loop()
        # if error_handler_loop is true, parse json data to python
        else:
            self.data = json.loads(response.text)

        return self

    # get graph name method - used for plotille graph name
    def get_graph_name(self, name: str) -> None:
        self.graph_name = self.data[0]["Country"]

    # get daily cases method
    def get_daily_cases(self) -> None:
        self.daily_cases = []

        # set counter to first Confirmed cases value (first
        # value being the 0th index)
        counter = self.data[0]["Confirmed"]

        # for loop to append the daily cases, which is calculated as
        # the difference between the existing Confirmed cases and
        # previous Confirmed cases (value of counter)
        for index in range(1, len(self.data)):
            new_daily_cases = self.data[index]["Confirmed"] - counter
            self.daily_cases.append(new_daily_cases)
            counter = self.data[index]["Confirmed"]

    # get daily deaths method
    def get_daily_deaths(self):
        self.daily_deaths = []

        # set counter to first Confirmed deaths value (first value being
        # the 0th index)
        counter = self.data[0]["Deaths"]

        # for loop to append the daily deaths, which is calculated as the
        # difference between the existing Confirmed deaths and previous
        # Confirmed deaths (value of counter)
        for index in range(1, len(self.data)):
            new_daily_deaths = self.data[index]["Deaths"] - counter
            self.daily_deaths.append(new_daily_deaths)
            counter = self.data[index]["Deaths"]

    # get cumulative deaths method
    def get_cumulative_deaths(self) -> None:
        self.cumulative_deaths = []

        # append confirmed number of deaths to cumulative deaths list as API
        # already provides cumulative number of deaths
        for number in range(0, len(self.data)):
            self.cumulative_deaths.append(self.data[number]["Deaths"])

    # get cumulative cases method
    def get_cumulative_cases(self) -> None:
        self.cumulative_cases = []

        # append confirmed number of cases to cumulative cases list as
        # API already provides cumulative number of cases
        for number in range(0, len(self.data)):
            self.cumulative_cases.append(self.data[number]["Confirmed"])

    # get fourteen day average method
    def get_fourteen_day_average_cases(self) -> None:
        self.fourteen_day_average_cases = []
        # for loop to go through daily cases data
        for index in range(1, len(self.daily_cases)+1):

            # if index is greater or equal to 14, sum the last 14 daily cases
            # and divide by 14 to get 14 day average.
            if index >= 14:
                self.fourteen_day_average_cases.append(
                    sum(self.daily_cases[index-14:index])//14)
            # else if index is less than 14, sum the last daily cases and
            # divide by the number of days/index already passed
            else:
                self.fourteen_day_average_cases.append(
                    sum(self.daily_cases[0:index])//(index))

    # get case fatality rate method
    def get_case_fatality_rate(self) -> None:
        self.case_fatality_rate = []

        # create a tuple list (cumulative deaths, cumulative cases) using the
        # zip function, to help calculate the case fatality rate
        case_fatality_rate_list = list(
            zip(self.cumulative_deaths, self.cumulative_cases))

        # for loop to go through cumulative deaths and cumlative
        # cases tuple list
        for cases_and_deaths in case_fatality_rate_list:
            # if cumulative cases is equal to 0, append 0 to case fatality
            # rate list to avoid zero division error
            if cases_and_deaths[1] == 0:
                self.case_fatality_rate.append(0)
            # in all other scenarios, we can calculate the case fatality
            # ratio by dividing cumulative deaths over cumulative cases,
            # multipled by 100 to return a percentage.
            else:
                self.case_fatality_rate.append(
                    cases_and_deaths[0] / cases_and_deaths[1]*100)
