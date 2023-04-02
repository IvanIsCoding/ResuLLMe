education_prompt = """
You are a career advisor at the Harvard Extension School. You are going to write a JSON resume section for an applicant applying for the following job post:
{JOB_POST_DESCRIPTION}

Consider the following CV:
{CV_TEXT}

Now consider the following JSON schema:
{
    "education": [
        {
            "institution": "Harvard University",
            "area": "Computer Science",
            "studyType": "Master's of Science",
            "startDate": "2011-01-01",
            "endDate": "2013-01-01",
            "score": "4.0"
        },
        {
            "institution": "University of California, Los Angeles",
            "area": "Computer Science",
            "studyType": "Bachelor of Science",
            "startDate": "2006-01-01",
            "endDate": "2010-01-01",
            "score": "3.25"
        }
    ]
}

Write the education section according to the schema. On the response, include only the JSON.
"""

awards_prompt = """
You are a career adviser at the Harvard Extension School. You are going to write a JSON resume section for an applicant applying for the following job post:
{JOB_POST_DESCRIPTION}

Consider the following CV:
{CV_TEXT}

Now consider the following JSON schema:
{
    "awards": [
        {
            "title": "TreeHacks 2019 Best Future of Education Hack",
            "date": "February, 2019",
            "awarder": "Stanford University",
            "summary": "Our project to match students from the Los Angeles School District with mentors at Ivy League schools won the award."
        },
        {
            "title": "HackTech 2018 Best Retro Hack",
            "date": "July 2018",
            "awarder": "California Institute of Technology",
            "summary": "Our project to create a virtual reality version of the 1980s arcade game 'Pong' won the award."
        }
    ]
}

Write the awards section according to the schema. Include only the awards section. On the response, include only the JSON.
"""

projects_prompt = """
You are a career advisor at the Harvard Extension School. You are going to write a JSON resume section for an applicant applying for the following job post:
{JOB_POST_DESCRIPTION}

Consider the following CV:
{CV_TEXT}

Now consider the following JSON schema:
{
    "projects": [
        {
            "name": "Harvard Lisp Experimental Compiler",
            "description": "A compiler for the Lisp programming language written in Haskell for CS510 to try functional programming on embedded systems. The compiler is open soruce and has over 500 stars on Github.",
            "keywords": ["Haskell", "Lisp", "Embedded Systems", "Arduino"],
            "url": "https://www.github.com/Harvard-SEAS-Alumn/hlec",
        },
        {
            "name": "New York Stock Exchange Arbtitrage Finder",
            "description": "A C++ program that finds arbitrage opportunities in the New York Stock Exchange using Bloomberg's API and low-latency network code.",
            "keywords": ["C++", "Bloomberg", "UDP", "Linux"],
            "url": "https://github.com/Harvard-SEAS/nyse-arbitrage-finder",
        }
    ]
}

Write the projects section according to the schema. Include only the most relevant projects to the job post on this section. On the response, include only the JSON.
"""

skills_prompt = """
You are a career advisor at the Harvard Extension School. You are going to write a JSON resume section for an applicant applying for the following job post:
{JOB_POST_DESCRIPTION}

Consider the following CV:
{CV_TEXT}

Now consider the following JSON schema:
{
    "skills": [
        {
            "name": "Programming Languages",
            "keywords": ["C", "C++", "Java", "JavaScript", "Haskell", "Clojure"]
        },
        {
            "name": "Frameworks"
            "keywords": ["React", "Vue", "Redux", "Spring", "Quarkus"]
        },
        {
            "name": "Certifications",
            "keywords": ["AWS Certified Solutions Architect", "AWS Certified Developer", "AWS Certified SysOps Administrator"]
        }
    ]
}

Write the skills section according to the schema. Include only the most relevant skills to the job post on this section. On the response, include only the JSON.
"""