import requests


def get_v1_account():
    """
    Get current user
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account"

    headers = {
      'X-Dm-Auth-Token': '<string>',
      'X-Dm-Bb-Render-Mode': '<string>',
      'Accept': 'text/plain'
    }

    response = requests.request(
        method="GET",
        url=url,
        headers=headers
    )

    return response
