import json
import urllib.parse

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from secret import (BASE_ID, BASE_PASSWORD, CALLBACK_URL, CLIENT_ID,
                    CLIENT_SECRET, SCOPE)

GET_AUTH_URL = 'https://api.thebase.in/1/oauth/authorize?response_type=' \
    'code&client_id=%ID%&redirect_uri=%URI%&scope=%SCOPE%'


def get_authorize_code():
    auth_url = GET_AUTH_URL.replace('%ID%', CLIENT_ID)
    auth_url = auth_url.replace(
        '%URI%', urllib.parse.quote(CALLBACK_URL, safe='')
    )
    auth_url = auth_url.replace(
        '%SCOPE%', urllib.parse.quote(SCOPE)
    )

    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    driver.get(auth_url)

    elem_login_id = driver.find_element(By.ID, 'UserMailAddress')
    elem_login_id.send_keys(BASE_ID)
    elem_login_password = driver.find_element(By.ID, 'UserPassword')
    elem_login_password.send_keys(BASE_PASSWORD)

    elem_auth_button = driver.find_element(By.NAME, 'auth_yes')
    elem_auth_button.click()

    code = driver.current_url.split("=")[1]
    driver.quit()

    return code


def get_access_token():
    auth_code = get_authorize_code()

    req_path = 'https://api.thebase.in/1/oauth/token'

    params = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': auth_code,
        'redirect_uri': CALLBACK_URL,
    }

    res = requests.post(req_path, params)
    token_data = json.loads(res.text)

    return token_data['access_token']
