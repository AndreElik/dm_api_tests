from pydantic import BaseModel, StrictStr, Field, Extra
from typing import Optional


class GeneralError(BaseModel):
    class Config:
        extra = Extra.forbid

    message: Optional[StrictStr] = Field(None, description='Client message')
