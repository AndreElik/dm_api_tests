from pydantic import BaseModel, StrictStr, Field


class ChangeRegisteredUserPasswordModel(BaseModel):
    login: StrictStr
    token: StrictStr
    old_password: StrictStr = Field(None, alias="oldPassword")
    new_password: StrictStr = Field(None, alias="newPassword")