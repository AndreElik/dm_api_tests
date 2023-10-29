from pydantic import BaseModel, StrictStr


class ChangeRegisteredUserEmailModel(BaseModel):
    login: StrictStr
    email: StrictStr
    password: StrictStr


