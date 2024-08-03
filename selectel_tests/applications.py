from selectel_tests.models.main_page_search import MainPageSearch
from selectel_tests.models.price_calculator_page import PriceCalculator
from selectel_tests.models.registration_page import RegistrationPage
from selectel_tests.models.sign_in_page import SignInPage


class ApplicationManager:
    def __init__(self):
        self.sign_in_page = SignInPage()
        self.registration_page = RegistrationPage()
        self.main_page_search = MainPageSearch()
        self.price_calculator = PriceCalculator()


app = ApplicationManager()
