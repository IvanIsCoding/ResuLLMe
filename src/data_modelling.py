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


class ResumeSkills(BaseModel):
    skills: Optional[List[ResumeSkillItem]] = Field(None, alias="skill_entry")

class ResumeWorkItem(BaseModel):
    company: Optional[str] = Field(None)
    position: Optional[str] = Field(None)
    startDate: Optional[str] = Field(None)
    endDate: Optional[str] = Field(None)
    location: Optional[str] = Field(None)
    highlights: Optional[List[str]] = Field(None)


class ResumeWork(BaseModel):
    work: Optional[List[ResumeWorkItem]] = Field(None, alias="work_experience")

class ResumeEducationItem(BaseModel):
    institution: Optional[str] = Field(None)
    area: Optional[str] = Field(None)
    additionalAreas: Optional[List[str]] = Field(None)
    studyType: Optional[str] = Field(None)
    startDate: Optional[str] = Field(None)
    endDate: Optional[str] = Field(None)
    score: Optional[str] = Field(None)
    location: Optional[str] = Field(None)


class ResumeEducation(BaseModel):
    education: Optional[List[ResumeEducationItem]] = Field(None, alias="education_entry")

class ResumeProjectItem(BaseModel):
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    keywords: Optional[List[str]] = Field(None)
    url: Optional[str] = Field(None)


class ResumeProjects(BaseModel):
    projects: Optional[List[ResumeProjectItem]] = Field(None, alias="project_entry")

class ResumeAwardItem(BaseModel):
    title: Optional[str] = Field(None)
    date: Optional[str] = Field(None)
    awarder: Optional[str] = Field(None)
    summary: Optional[str] = Field(None)


class ResumeAwards(BaseModel):
    awards: List[ResumeAwardItem] = Field(None, alias="award_entry")

class Resume(BaseModel):
    basics: ResumeBasics = Field(...)
    skills: Optional[ResumeSkills] = Field(...)
    work: Optional[ResumeWork] = Field(...)
    education: Optional[ResumeEducation] = Field(...)
    projects: Optional[ResumeProjects] = Field(...)
    awards: Optional[ResumeAwards] = Field(...)