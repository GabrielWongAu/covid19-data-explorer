import plotille
import os

from country import Country
#TERMX, TERMY = os.get_terminal_size()


# country class to display various graphs
class DisplayGraph:
    # display total deaths method to animate graph of cumulative deaths
    def display_total_deaths(
            self, country_total_deaths: Country, x_axis_days_data: list,
            y_axis_cumulative_deaths: list) -> None:
        from screens import print_centred
        import replit
        import time

        # instantiate total deaths plotille graph
        figure_total_deaths = plotille.Figure()

        # set heigh and width of the plotille graph
        figure_total_deaths.width = 130
        figure_total_deaths.height = 25

        # set color mode of plotille graph to names
        figure_total_deaths.color_mode = "names"

        # set x axis label to days
        figure_total_deaths.x_label = "days"

        # set y axis label to deaths
        figure_total_deaths.y_label = "deaths"

        # set graph so x=0 and y=0
        figure_total_deaths.set_x_limits(min_=0)
        figure_total_deaths.set_y_limits(min_=0)

        # command to not print the dotted x and y origins
        figure_total_deaths.origin = False

        # for loop to animate the total deaths graph - update x
        # and y axis list data, clear screen & plotille graph, add
        # data to plotille graph, print new plotille graph, rinse and repeat
        for index in range(0, len(country_total_deaths.data)):
            # update y_axis_cumulative_deaths list with next index data
            y_axis_cumulative_deaths.append(
                country_total_deaths.data[index]["Deaths"])

            # update x_axis_days_data list with next index
            x_axis_days_data.append(index)

            # clear the screen
            replit.clear()

            # remove all plots from the total deaths plotille graph
            figure_total_deaths.clear()

            # add data to existing total deaths plotille graph
            figure_total_deaths.scatter(
                x_axis_days_data, y_axis_cumulative_deaths, lc="magenta",
                label=f"{country_total_deaths.graph_name}")

            # print graph header
            print_centred("Cumulative Deaths")

            # print new total deaths plotille graph with updated data
            print(figure_total_deaths.show(legend=True))

            # suspend execution for 0.1 seconds
            time.sleep(.1)

    # display fourteen day average graph method to animate graph of fourteen
    # day case average
    def display_fourteen_day_average_graph(
            self, country_fourteen_day_average: Country,
            x_axis_days_data: list,
            y_axis_fourteen_day_average_cases: list) -> None:
        from screens import print_centred
        import replit
        import time

        # instantiate fourteen day case average plotille graph
        figure_fourteen_day_average_cases = plotille.Figure()

        # set heigh and width of the plotille graph
        figure_fourteen_day_average_cases.width = 130
        figure_fourteen_day_average_cases.height = 25

        # set color mode of plotille graph to names
        figure_fourteen_day_average_cases.color_mode = "names"

        # set x axis label to days
        figure_fourteen_day_average_cases.x_label = "days"

        # set y axis label to cases
        figure_fourteen_day_average_cases.y_label = "cases"

        # set graph so x=0 and y=0
        figure_fourteen_day_average_cases.set_x_limits(min_=0)
        figure_fourteen_day_average_cases.set_y_limits(min_=0)

        # command to not print the dotted x and y origins
        figure_fourteen_day_average_cases.origin = False

        # for loop to animate the fourteen day average graph - update x and y
        # axis list data, clear screen & plotille graph, add data to plotille
        # graph, print new plotille graph, rinse and repeat
        for index in range(1, len(country_fourteen_day_average.daily_cases)+1):
            # if index is greater or equal to 14, sum the last 14 daily cases
            # and divide by 14 to get 14 day average.
            if index >= 14:
                y_axis_fourteen_day_average_cases.append(
                    sum(country_fourteen_day_average.daily_cases
                        [index-14:index])//14)
            # else if index is less than 14, sum the previous daily cases and
            # divide by the number of days/index already passed
            else:
                y_axis_fourteen_day_average_cases.append(
                    sum(country_fourteen_day_average.daily_cases[0:index])//(
                        index))

            x_axis_days_data.append(index)

            # clear the screen
            replit.clear()

            # remove all plots from the fourteen day average cases
            # plotille graph
            figure_fourteen_day_average_cases.clear()

            # add new data to existing fourteen day average cases
            # plotille graph
            figure_fourteen_day_average_cases.scatter(
                x_axis_days_data, y_axis_fourteen_day_average_cases,
                lc='blue',
                label=f'{country_fourteen_day_average.graph_name}')

            # print graph header
            print_centred("14 Day Average Cases")

            # print new fourteen day average cases plotille graph with
            # updated data
            print(figure_fourteen_day_average_cases.show(legend=True))

            # suspend execution for 0.1 seconds
            time.sleep(.1)

    # display case fatality rate method to animate graph of case fatality rate
    def display_case_fatality_rate(
        self, country_case_fatality_rate: Country,
            x_axis_days_data: list,
            y_axis_case_fatality_rate_data: list) -> None:
        from screens import print_centred
        import replit
        import time

        # instantiate case fatality rate plotille graph
        figure_case_fatality_rate = plotille.Figure()

        # set heigh and width of the plotille graph
        figure_case_fatality_rate.width = 130
        figure_case_fatality_rate.height = 25

        # set color mode of plotille graph to names
        figure_case_fatality_rate.color_mode = "names"

        # set x axis label to days
        figure_case_fatality_rate.x_label = "days"

        # set y axis label to %
        figure_case_fatality_rate.y_label = "%"

        # set graph so x=0 and y=0
        figure_case_fatality_rate.set_x_limits(min_=0)
        figure_case_fatality_rate.set_y_limits(min_=0)

        # command to not print the dotted x and y origins
        figure_case_fatality_rate.origin = False

        # create a tuple list (cumulative deaths, cumulative cases) using
        # the zip function, to help calculate the case fatality rate
        case_fatality_rate_list = list(zip(
            country_case_fatality_rate.cumulative_deaths,
            country_case_fatality_rate.cumulative_cases))
        day = 0

        # for loop to animate the case fatality ratio graph - update x and
        # y axis list data, clear screen & plotille graph, add data to
        # plotille graph, print new plotille graph, rinse and repeat
        for cases_and_deaths in case_fatality_rate_list:

            # if cumulative cases is equal to 0, append 0 to avoid zero
            # division error
            if cases_and_deaths[1] == 0:
                y_axis_case_fatality_rate_data.append(0)

            # in all other scenarios, we can calculate the case fatality
            # ratio by dividing cumulative deaths over cumulative cases,
            # multipled by 100 to return a percentage.
            else:
                y_axis_case_fatality_rate_data.append(
                    cases_and_deaths[0] / cases_and_deaths[1]*100)

            # update x_axis_days_data list with next index
            x_axis_days_data.append(day)
            day = day + 1

            # clear the screen
            replit.clear()

            # remove all plots from the case fatality rate plotille graph
            figure_case_fatality_rate.clear()

            # add data to existing case fatality ratio plotille graph
            figure_case_fatality_rate.scatter(
                x_axis_days_data, y_axis_case_fatality_rate_data, lc='green',
                label=f'{country_case_fatality_rate.graph_name}')

            # print graph header
            print_centred("Case Fatality Rate")

            # print new case fatality rate plotille graph with updated data
            print(figure_case_fatality_rate.show(legend=True))

            # suspend execution for 0.1 seconds
            time.sleep(.1)
