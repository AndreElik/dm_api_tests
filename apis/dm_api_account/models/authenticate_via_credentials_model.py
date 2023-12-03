from pydantic import BaseModel, StrictStr, Field, StrictBool


class AuthenticateViaCredentialsModel(BaseModel):
    login: StrictStr
    password: StrictStr
    remember_me: StrictBool = Field(None, alias='rememberMe')


