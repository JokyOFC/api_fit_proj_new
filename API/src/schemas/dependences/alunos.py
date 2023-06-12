# -*- coding: utf-8 -*-

from pydantic import BaseModel
from typing import Optional

class Aluno(BaseModel):
    user_id: Optional[int] = None
    nome: str
    cpf: str
    data_de_nascimento: str
    
    
class DadosContatosAluno(BaseModel):
    telefone: str
    telefone_alt: str
    email: str
    endereco: str

class TipoCorpo(BaseModel):
    tipo: str
    media_peso: int
    media_altura: int
    media_gordura: int
    media_massa_corporea: int
    media_consumo: int
    media_hormonios: int