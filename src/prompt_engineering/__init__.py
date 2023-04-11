basics_prompt = """
You are going to write a JSON resume section for an applicant applying for job posts.

Consider the following CV:
<CV_TEXT>

Now consider the following TypeScript Interface for the JSON schema:

interface Basics {
    name: string;
    email: string;
    phone: string;
    website: string;
    address: string;
}

Write the basics section according to the Basic schema. On the response, include only the JSON.
"""

education_prompt = """
You are going to write a JSON resume section for an applicant applying for job posts.

Consider the following CV:
<CV_TEXT>

Now consider the following TypeScript Interface for the JSON schema:

interface EducationItem {
    institution: string;
    area: string;
    studyType: string;
    startDate: string;
    endDate: string;
    score: string;
    location: string;
}

interface Education {
    education: EducationItem[];
}


Write the education section according to the Education schema. On the response, include only the JSON.
"""

awards_prompt = """
You are a career adviser at the Harvard Extension School. You are going to write a JSON resume section for an applicant applying for job posts.

Consider the following CV:
<CV_TEXT>

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
You are a career adviser at the Harvard Extension School. You are going to write a JSON resume section for an applicant applying for job posts.

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

Write the projects section according to the schema. Include all projects, but only the ones present in the CV. On the response, include only the JSON.
"""

skills_prompt = """
You are a career adviser at the Harvard Extension School. You are going to write a JSON resume section for an applicant applying for job posts.

Consider the following CV:
<CV_TEXT>

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

Notice that the schema is a list of skills. Each skill has a name and a list of keywords. This is extremely flexible, as the following is also valid:
{
    "skills": [
        {
            "name": "Relevant Coursework",
            "keywords": ["Econometrics", "Quantitative Political Science", "Applied Machine Learning for the Social Sciences", "Mathematical Finance"]
        },
        {
            "name": "Computer Software"
            "keywords": ["Microsoft Excel", "Microsoft Word", "Microsoft Power Point", "Stata", "Matlab"]
        },
        {
            "name": "Foreign Languages",
            "keywords": ["French (Fluent)", "Chinese (Intermediate)", "Arabic (Beginner)"]
        }
    ]
}

Write the skills section according to the schema. Include all skills, but only the ones present in the CV. On the response, include only the JSON.
"""

work_prompt = """
You are a career adviser at the Harvard Extension School. You are going to write a JSON resume section for an applicant applying for job posts.

Consider the following CV:
<CV_TEXT>

Write a work experience section for the candidate. Include only the work experience and not the project experience. For each work experience, provide  a company name, position name, start and end date, and bullet point for the highlights. Follow the Harvard Extension School Resume guidelines and phrase the bullet points with the STAR methodology

Work Experience:
"""