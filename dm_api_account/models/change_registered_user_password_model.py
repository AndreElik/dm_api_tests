from pydantic import BaseModel, StrictStr, Field


class ChangeRegisteredUserPasswordModel(BaseModel):
    login: StrictStr
    token: StrictStr
    old_password: StrictStr = Field(None, alias="oldPassword", description='Old password')
    new_password: StrictStr = Field(None, alias="newPassword", description='New password')

    def printing_field(self):
        print(self.old_password)
