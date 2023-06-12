# -*- coding: utf-8 -*-

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt"])

def verifyPassword(text: str, hash) -> bool:
    return pwd_context.verify(text, hash)

def getPasswordHash(password: str) -> str:
    return pwd_context.hash(password)

