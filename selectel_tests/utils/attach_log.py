import logging
import os

import allure
from allure_commons.types import AttachmentType
from requests import Response

from selectel_tests.utils.format_view import pretty_headers, pretty_body


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    log = ''.join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(body=log, name='browser_logs', attachment_type=AttachmentType.TEXT, extension='.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(body=html, name='page_source', attachment_type=AttachmentType.HTML, extension='.html')


def add_video(browser):
    session_id = browser.driver.session_id
    video_url = f"https://{os.getenv('SELENOID_URL')}/video/" + session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(body=html, name='video_' + session_id, attachment_type=AttachmentType.HTML, extension='.html')


def allure_request_logger(function):
    def wrapper(*args, **kwargs):
        response: Response = function(*args, **kwargs)

        logging.info(f'\n\nREQUEST {response.request.method} {response.request.url}\n'
                     f'\nREQUEST HEADERS: \n{pretty_headers(response.request.headers)}\n'
                     f'\nREQUEST BODY: \n{pretty_body(response.request.body)}\n'
                     f'\nRESPONSE HEADERS: \n{pretty_headers(response.headers)}\n'
                     f'\nRESPONSE BODY: \n{pretty_body(response.text)}\n')
        return response

    return wrapper
