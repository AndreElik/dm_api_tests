from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr
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
    quality: int
    quantity: int


class BbParseMode(Enum):
    COMMON = 'Common'
    INFO = 'Info'
    POST = 'Post'
    CHAT = 'Chat'


class Info(BaseModel):
    value: Optional[StrictStr] = Field(None)
    parse_mode: BbParseMode


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
    icq: Optional[StrictStr] = Field(None)
    skype: Optional[StrictStr] = Field(None)
    original_picture_url: Optional[StrictStr] = Field(None, alias='originalPictureUrl')
    info: Optional[Info]


class UserDetailsEnvelopeModel(BaseModel):
    resource: User
    metadata: Optional[StrictStr] = Field(None)