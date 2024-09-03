from selectel_tests.models.pages.main_page_search import MainPageSearch
from selectel_tests.models.pages.price_calculator_page import PriceCalculator
from selectel_tests.models.pages.registration_page import RegistrationPage
from selectel_tests.models.pages.sign_in_page import SignInPage


class ApplicationManager:
    def __init__(self):
        self.sign_in_page = SignInPage()
        self.registration_page = RegistrationPage()
        self.main_page_search = MainPageSearch()
        self.price_calculator = PriceCalculator()


app = ApplicationManager()
