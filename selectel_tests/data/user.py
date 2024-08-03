import os
from dataclasses import dataclass

@dataclass
class UserRegForm:
    email: str
    password: str
    give_personal_data: bool
    receive_news: bool


@dataclass
class UserSignIn:
    account_number: str
    password: str


user_for_registration_form = UserRegForm(
    email='example@yahoo.com',
    password='UaUaUa123456',
    give_personal_data=True,
    receive_news=False
)

user_for_registration_form_with_wrong_data = UserRegForm(
    email='example',
    password='Kuku',
    give_personal_data=True,
    receive_news=False
)

user_for_registration_form_with_empty_data = UserRegForm(
    email='',
    password='',
    give_personal_data=False,
    receive_news=False
)

user_for_sign_in_without_phone_number = UserSignIn(
    account_number='335553',
    password='QaQa4321'
)

user_for_sign_in_with_wrong_password = UserSignIn(
    account_number='335553',
    password='Kuku123456789'
)

user_for_sign_in_with_phone_number = UserSignIn(
    account_number='335938',
    password='LaLaLa1234'
)
