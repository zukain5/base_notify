import urllib.parse
from selenium import webdriver
from secret import CLIENT_ID, CLIENT_SECRET, CALLBACK_URL, \
    SCOPE, DRIVER_PATH, BASE_ID, BASE_PASSWORD

# 参考: https://rabbitfoot.xyz/baseapi-getproductlist-withpython-1/

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

    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(auth_url)

    elem_login_id = driver.find_element_by_id('UserMailAddress')
    elem_login_id.send_keys(BASE_ID)
    elem_login_password = driver.find_element_by_id('UserPassword')
    elem_login_password.send_keys(BASE_PASSWORD)

    elem_auth_button = driver.find_element_by_name('auth_yes')
    elem_auth_button.click()

    code = driver.current_url.split("=")[1]
    driver.quit()

    return code
