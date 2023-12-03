from typing import List, Optional
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
    quality: int
    quantity: int


class BbParseMode(Enum):
    COMMON = 'Common'
    INFO = 'Info'
    POST = 'Post'
    CHAT = 'Chat'


class InfoBbText(BaseModel):
    value: Optional[StrictStr] = None
    parse_mode: Optional[BbParseMode] = Field(None, alias='parseMode')


class ColorSchema(Enum):
    MODERN = 'Modern'
    PALE = 'Pale'
    CLASSIC = 'Classic'
    CLASSIC_PALE = 'ClassicPale'
    NIGHT = 'Night'


class PagingSetting(BaseModel):
    posts_per_page: Optional[StrictInt] = Field(None, alias='postsPerPage')
    comments_per_page: Optional[StrictInt] = Field(None, alias='commentsPerPage')
    topics_per_page: Optional[StrictInt] = Field(None, alias='topicsPerPage')
    messages_per_page: Optional[StrictInt] = Field(None, alias='messagesPerPage')
    entities_per_page: Optional[StrictInt] = Field(None, alias='entitiesPerPage	')


class UserSettings(BaseModel):
    color_schema: Optional[ColorSchema] = Field(None, alias='colorSchema')
    nanny_greetings_message: Optional[StrictStr] = Field(None, alias='nannyGreetingsMessage')
    paging: Optional[PagingSetting]


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
    info: Optional[StrictStr] = Field(None)
    settings: Optional[UserSettings]


class UserDetailsEnvelopeModel(BaseModel):
    resource: User
    metadata: Optional[StrictStr] = Field(None)