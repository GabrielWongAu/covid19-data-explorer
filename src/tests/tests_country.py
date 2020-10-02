import unittest
import json
import requests
#from unittest.mock import patch
#import pytest
from country import Country


class TestCase(unittest.TestCase):

    # #Unit Test
    # @patch('requests.get')
    # def test_exception(mock_run):
    #     mock_run.side_effect = requests.exceptions.ConnectionError()
    #     with pytest.raises(SystemExit) as sys_exit:
    #       method_to_test()
    #     assert 'Error ' in str(sys_exit.value) 

    # #Method to Test
    # def method_to_test():
    #     try:
    #         # ADD EXCEPTION HERE
    #         raise requests.exceptions.HTTPError('Throwing an exception here!')
    #         response = requests.get('some_url', verify=False, stream=True)
    #         response.raise_for_status()
    #     except (requests.exceptions.HTTPError,
    #             requests.exceptions.ConnectionError,
    #             requests.exceptions.Timeout) as err:
    #         # err will now be 'Throwing an exception here!'
    #         msg = f'Failure: {err}' # Here err is always empty
    #         raise SystemExit(msg)

    def test_get_daily_cases(self):
        country = Country("TEST")
        with open("./tests/data/australiadata.json", "r") as filehandler:
            country.data = json.loads(filehandler.readline())

        country.get_daily_cases()

        self.assertEqual(country.daily_cases, [9, 13, 3, 5])

    def test_get_daily_deaths(self):
        country = Country("TEST")
        with open("./tests/data/australiadata.json", "r") as filehandler:
            country.data = json.loads(filehandler.readline())

        country.get_daily_deaths()

        self.assertEqual(country.daily_deaths, [0, 1, 0, 0])


    def test_get_cummulative_deaths(self):
        country = Country("TEST")
        with open("./tests/data/australiadata.json", "r") as filehandler:
            country.data = json.loads(filehandler.readline())

        country.get_cumulative_deaths()

        self.assertEqual(country.cumulative_deaths, [1, 1, 2, 2, 2])

    def test_get_cummulative_cases(self):
        country = Country("TEST")
        with open("./tests/data/australiadata.json", "r") as filehandler:
            country.data = json.loads(filehandler.readline())

        country.get_cumulative_cases()

        self.assertEqual(country.cumulative_cases, [30, 39, 52, 55, 60])

    def test_get_fourteen_day_average(self):
        country = Country("TEST")
        with open("./tests/data/fourteen_day_average_australia_data.json", "r") as filehandler:
            country.data = json.loads(filehandler.readline())

        country.get_daily_cases()
        country.get_fourteen_day_average_cases()

        self.assertEqual(country.fourteen_day_average_cases, [7,9,7,6,10,11,11,12,13,14,13,16,15,16,17,19,21])


    def test_get_case_fatality_rate(self):
        country = Country("TEST")
        with open("./tests/data/australiadata.json", "r") as filehandler:
            country.data = json.loads(filehandler.readline())

        country.get_cumulative_cases()
        country.get_cumulative_deaths()
        country.get_case_fatality_rate()

        self.assertEqual(country.case_fatality_rate, [1/30*100, 1/39*100, 2/52*100, 2/55*100, 2/60*100])


