import requests
import json


def post_v1_account():
    """
    Authenticate via credentials
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/login"

    payload = {
      "login": "user_252",
      "email": "user_252@gmail.com",
      "password": "123456qwerty"
    }
    headers = {
      'X-Dm-Bb-Render-Mode': '<string>',
      'Content-Type': 'application/json',
      'Accept': 'text/plain'
    }

    response = requests.request(
        method="POST",
        url=url,
        headers=headers,
        json=payload
    )

    return response
