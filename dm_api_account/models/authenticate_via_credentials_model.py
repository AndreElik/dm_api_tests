from pydantic import BaseModel, StrictStr


class AuthenticateViaCredentialsModel(BaseModel):
    login: StrictStr
    email: StrictStr
    password: StrictStr
