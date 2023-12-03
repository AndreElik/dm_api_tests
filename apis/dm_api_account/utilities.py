import allure
import requests
from pydantic import BaseModel


def validate_request_json(json: str | BaseModel):
    if isinstance(json, dict):
        return json
    return json.model_dump(
        by_alias=True,
        exclude_none=True
    )


def validate_status_code(response: requests.Response, status_code: int):
    with allure.step('Проверка валидации и статус-кода'):
        assert response.status_code == status_code, \
            f'статус код ответа должен быть {status_code}, но он равен {response.status_code}'
