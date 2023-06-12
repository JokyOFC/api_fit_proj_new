# -*- coding: utf-8 -*-

from pydantic import BaseModel

class Logs(BaseModel):
    data_hora: str
    users_user_fk: int
    descricao: str