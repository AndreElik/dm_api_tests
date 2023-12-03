from typing import List, Optional, Any
from pydantic import BaseModel, Field, StrictStr, StrictInt
from enum import Enum
from datetime import datetime


class Roles(Enum):
    GUEST = 'Guest'
    PLAYER = 'Player'
    ADMINISTRATOR = 'Administrator'
    NANNY_MODERATOR = 'NannyModerator'
    REGULAR_MODERATOR = 'RegularModerator'
    SENIOR_MODERATOR = 'SeniorModerator'


class Rating(BaseModel):
    enabled: bool
    quality: StrictInt
    quantity: StrictInt


class User(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(None, alias='mediumPictureUrl')
    small_picture_url: Optional[StrictStr] = Field(None, alias='smallPictureUrl')
    status: Optional[StrictStr] = Field(None)
    rating: Rating
    online: datetime = Field(None)
    name: Optional[StrictStr] = Field(None)
    location: Optional[StrictStr] = Field(None)
    registration: datetime = Field(None)


class UserEnvelopeModel(BaseModel):
    resource: User
    metadata: Optional[Any] = Field(None, description='Additional metadata')

