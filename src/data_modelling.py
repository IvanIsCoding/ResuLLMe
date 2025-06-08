from pydantic import BaseModel, Field
from typing import Optional, List


class ResumeBasics(BaseModel):
    name: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    phone: Optional[str] = Field(None)
    website: Optional[str] = Field(None)
    address: Optional[str] = Field(None)


class ResumeSkillItem(BaseModel):
    name: str = Field(...)
    keywords: Optional[List[str]] = Field(None)


class ResumeWorkItem(BaseModel):
    company: Optional[str] = Field(None)
    position: Optional[str] = Field(None)
    startDate: Optional[str] = Field(None)
    endDate: Optional[str] = Field(None)
    location: Optional[str] = Field(None)
    highlights: Optional[List[str]] = Field(None)


class ResumeEducationItem(BaseModel):
    institution: Optional[str] = Field(None)
    area: Optional[str] = Field(None)
    additionalAreas: Optional[List[str]] = Field(None)
    studyType: Optional[str] = Field(None)
    startDate: Optional[str] = Field(None)
    endDate: Optional[str] = Field(None)
    score: Optional[str] = Field(None)
    location: Optional[str] = Field(None)


class ResumeProjectItem(BaseModel):
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    keywords: Optional[List[str]] = Field(None)
    url: Optional[str] = Field(None)


class ResumeAwardItem(BaseModel):
    title: Optional[str] = Field(None)
    date: Optional[str] = Field(None)
    awarder: Optional[str] = Field(None)
    summary: Optional[str] = Field(None)


class Resume(BaseModel):
    basics: Optional[ResumeBasics] = Field(None)
    skills: Optional[List[ResumeSkillItem]] = Field(None)
    work: Optional[List[ResumeWorkItem]] = Field(None)
    education: Optional[List[ResumeEducationItem]] = Field(None)
    projects: Optional[List[ResumeProjectItem]] = Field(None)
    awards: Optional[List[ResumeAwardItem]] = Field(None)
