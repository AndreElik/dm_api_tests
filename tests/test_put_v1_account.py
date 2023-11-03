import requests
import structlog
from services.dm_api_account import DmApiAccount
from dm_api_account.models.user_evelope_model import User, Roles, Rating
from hamcrest import assert_that, has_properties


structlog.configure(processors=[structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)])


def test_put_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    token = '63010389-8550-456a-bd62-67c8e07de400'
    response = api.account.put_v1_account(token=token, status_code=200)
    assert_that(response.resource, has_properties(
        {"login": "user_304",
         "roles": [Roles.GUEST, Roles.PLAYER]
         }
    ))
    assert_that(response.resource.rating, has_properties(
        {"enabled": True,
         "quality": 0,
         "quantity": 0
         }
    ))


