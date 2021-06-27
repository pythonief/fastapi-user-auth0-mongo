from typing import Dict, List

from app.utils import *
from fastapi import Depends
from pydantic import BaseModel
from pydantic.networks import EmailStr


class Contact(BaseModel):
    email: EmailStr = ''
    address: Dict[str, str] = {}
    phone_number: str


class Job(BaseModel):
    name: str
    company: str = ''
    start: str
    end: str = 'present'
    description: str = ''


class Skill(BaseModel):
    name: str
    description: str = ''


class Reference(BaseModel):
    name: str
    email: EmailStr
    phone_number: str = ''
    company_name: str = ''


class Curriculum(BaseModel):
    contact: Depends(Contact) = {}
    about_description: str = ''
    job_exp: List[Job] = []
    skills: List[Skill] = []
    referencies: List[Reference] = []


class ShowCurriculum(Curriculum, MongoMixinBaseModel):
    """Class just for issue throw the api response to the client
    """
    pass
