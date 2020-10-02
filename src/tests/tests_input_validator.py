import unittest
from input_validator import validate_country_input
from input_validator import validate_menu_selection
from input_validator import validate_data_explorer_restart


class TestCase_Input_Validator(unittest.TestCase):

    # Tests for Validate Country Input

    def test_validate_correct_country_name(self):
        result = validate_country_input("Australia")
        self.assertEqual(result, True, msg="Result did not return True")

    def test_validate_correct_country_name_mixed_letters(self):
        result = validate_country_input("AuStRaLiA")
        self.assertEqual(result, True, msg="Result did not return True")

    def test_validate_correct_country_name_lowercase(self):
        result = validate_country_input("australia")
        self.assertEqual(result, True, msg="Result did not return True")

    def test_validate_correct_country_code(self):
        result = validate_country_input("AU")
        self.assertEqual(result, True, msg="Result did not return True")

    def test_validate_correct_country_code_incorrect(self):
        result = validate_country_input("AU1231")
        self.assertEqual(result, False, msg="Result did not return True")

    def test_validate_incorrect_input(self):
        result = validate_country_input("ASDASDASD")
        self.assertEqual(result, False, msg="Result did not return False")

    def test_validate_incorrect_symbols(self):
        result = validate_country_input("*(%&*)()()")
        self.assertEqual(result, False, msg="Result did not return False")

    def test_validate_incorrect_empty(self):
        result = validate_country_input("")
        self.assertEqual(result, False, msg="Result did not return False")

    # Tests for Validate Menu Selection

    def test_validate_correct_menu_selection_one(self):
        result = validate_menu_selection("1")
        self.assertEqual(result, "1", msg="Result did not return 1")

    def test_validate_correct_menu_selection_two(self):
        result = validate_menu_selection("2")
        self.assertEqual(result, "2", msg="Result did not return 2")

    def test_validate_correct_menu_selection_three(self):
        result = validate_menu_selection("3")
        self.assertEqual(result, "3", msg="Result did not return 3")

    def test_validate_correct_menu_selection_four(self):
        result = validate_menu_selection("4")
        self.assertEqual(result, "4", msg="Result did not return 4")

    def test_validate_incorrect_menu_selection_letter(self):
        result = validate_menu_selection("A")
        self.assertEqual(result, False, msg="Result did not return False")

    def test_validate_incorrect_menu_selection_symbol(self):
        result = validate_menu_selection("%")
        self.assertEqual(result, False, msg="Result did not return False")

    def test_validate_incorrect_menu_selection_empty(self):
        result = validate_menu_selection("")
        self.assertEqual(result, False, msg="Result did not return False")

    # Tests for Validate Data Explorer Restart

    def test_validate_data_explorer_lowcase_y(self):
        result = validate_data_explorer_restart("y")
        self.assertEqual(result, True, msg="Result did not return True")

    def test_validate_data_explorer_uppercase_yy(self):
        result = validate_data_explorer_restart("Y")
        self.assertEqual(result, True, msg="Result did not return True")

    def test_validate_data_explorer_lowercase_n(self):
        result = validate_data_explorer_restart("n")
        self.assertEqual(result, False, msg="Result did not return True")

    def test_validate_data_explorer_uppercase_n(self):
        result = validate_data_explorer_restart("N")
        self.assertEqual(result, False, msg="Result did not return True")
