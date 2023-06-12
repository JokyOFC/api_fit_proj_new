# -*- coding: utf-8 -*-

from pydantic import BaseModel
from typing import Optional

class UserResponse(BaseModel):
    user_id: Optional[int] = None
    username : Optional[str]  = None
    email : Optional[str ] = None
    