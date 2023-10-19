import requests


def put_v1_account():
    """
    Activate registered user
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/564e9e0e-3232-4f00-ac72-056f616aabd6"

    headers = {
      'X-Dm-Auth-Token': '<string>',
      'X-Dm-Bb-Render-Mode': '<string>',
      'Accept': 'text/plain'
    }

    response = requests.request(
        method="PUT",
        url=url,
        headers=headers
    )

    return response
