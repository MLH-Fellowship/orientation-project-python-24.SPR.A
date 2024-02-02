# pylint: disable=R0913

'''
Models for the Resume API. Each class is related to
'''

from dataclasses import dataclass


@dataclass
class Experience:
    '''
    Experience Class
    '''
    id: int
    title: str
    company: str
    start_date: str
    end_date: str
    description: str
    logo: str


@dataclass
class Education:
    '''
    Education Class
    '''
    id: int
    course: str
    school: str
    start_date: str
    end_date: str
    grade: str
    logo: str


@dataclass
class Skill:
    '''
    Skill Class
    '''
    id: int
    name: str
    proficiency: str
    logo: str
