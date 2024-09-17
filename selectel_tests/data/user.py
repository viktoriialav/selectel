import os
from dataclasses import dataclass
import dotenv

dotenv.load_dotenv()

@dataclass
class UserRegForm:
    email: str
    password: str
    repeat_password: str
    give_personal_data: bool
    receive_news: bool


@dataclass
class UserSignIn:
    account_number: str
    password: str


user_for_registration_form = UserRegForm(
    email='example@yahoo.com',
    password='UaUaUa123456',
    repeat_password='UaUaUa123456',
    give_personal_data=True,
    receive_news=False
)

user_for_registration_form_with_wrong_data = UserRegForm(
    email='example',
    password='Kuku',
    repeat_password='KukuKuku',
    give_personal_data=True,
    receive_news=False
)

user_for_registration_form_with_empty_data = UserRegForm(
    email='',
    password='',
    repeat_password='',
    give_personal_data=False,
    receive_news=False
)

user_for_sign_in_without_two_step_auth = UserSignIn(
    account_number=os.getenv('account_number_without_two_step_auth'),
    password=os.getenv('password_without_two_step_auth')
)

user_for_sign_in_with_wrong_password = UserSignIn(
    account_number=os.getenv('account_number_without_two_step_auth'),
    password='Kuku123456789'
)

user_for_sign_in_with_two_step_auth = UserSignIn(
    account_number=os.getenv('account_number_with_two_step_auth'),
    password=os.getenv('password_with_two_step_auth')
)
