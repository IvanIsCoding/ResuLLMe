from pydantic import BaseModel, Field
from typing import Optional, List

class ResumeBasics(BaseModel):
    name: str = Field(...)
    email: Optional[str] = Field(None)
    phone: Optional[str] = Field(None)
    website: Optional[str] = Field(None)
    address: Optional[str] = Field(None)

class ResumeEducationItem(BaseModel):
    institution: str = Field(...)
    area: Optional[str] = Field(None)
    additionalAreas: Optional[List[str]] = Field(None)
    studyType: Optional[str] = Field(None)
    startDate: Optional[str] = Field(None)
    endDate: Optional[str] = Field(None)
    score: Optional[str] = Field(None)
    location: Optional[str] = Field(None)


class ResumeEducation(BaseModel):
    education: List[ResumeEducationItem] = Field(..., alias="education entry")

class ResumeProjectItem(BaseModel):
    name: str = Field(...)
    description: Optional[str] = Field(None)
    keywords: Optional[List[str]] = Field(None)
    url: Optional[str] = Field(None)


class Projects(BaseModel):
    projects: List[ResumeProjectItem] = Field(None)

class ResumeAwardItem(BaseModel):
    title: str = Field(...)
    date: Optional[str] = Field(None)
    awarder: Optional[str] = Field(None)
    summary: Optional[str] = Field(None)


class ResumeAwards(BaseModel):
    awards: List[ResumeAwardItem] = Field(default_factory=list)

class Resume(BaseModel):
    basics: ResumeBasics = Field(...)
    education: ResumeEducation = Field(...)
    projects: Projects = Field(...)
    awards: ResumeAwards = Field(...)