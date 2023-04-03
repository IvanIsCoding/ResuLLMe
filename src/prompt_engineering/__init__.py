basics_prompt = """
You are a career advisor at the Harvard Extension School. You are going to write a JSON resume section for an applicant applying for job posts.

Consider the following CV:
<CV_TEXT>

Now consider the following JSON schema:
{
    "basics": {
        "name": "John Doe",
        "email": "john@gmail.com",
        "phone": "(912) 555-4321",
        "website": "https://johndoe.com",
        "location": "Atlanta, GA"
    }
}

Write the basics section according to the schema. On the response, include only the JSON.
"""

education_prompt = """
You are a career advisor at the Harvard Extension School. You are going to write a JSON resume section for an applicant applying for job posts.

Consider the following CV:
<CV_TEXT>

Now consider the following JSON schema:
{
    "education": [
        {
            "institution": "Harvard University",
            "area": "Computer Science",
            "studyType": "Master's of Science",
            "startDate": "January 2011",
            "endDate": "December 2012",
            "score": "4.0",
            "location": "Cambridge, MA"
        },
        {
            "institution": "University of California, Los Angeles",
            "area": "Computer Science",
            "studyType": "Bachelor of Science",
            "startDate": "September 2005",
            "endDate": "June 2009",
            "score": "3.25",
            "location": "Los Angeles, CA"
        }
    ]
}

Write the education section according to the schema. On the response, include only the JSON.
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

Now consider the following JSON schema:
{
    "work": [
        {
            "company": "Apple",
            "position": "Senior Software Engineer",
            "startDate": "January 2018",
            "endDate": "Present",
            "highlights": [
                "Developed a new feature for the Apple Watch that allows users to track their heart rate and sleep patterns, saving a famous twitter influencer from a heart attack",
                "Created the step counting feature in the Apple, leading to over a trillion steps being counted by the Apple Watch",
                "Made the Mickey Mouse watch face, putting a smile on the faces of millions of users"
            ]
        },
        {
            "company": "Snap",
            "position": "Software Engineer",
            "startDate": "March 2014",
            "endDate": "December 2018",
            "highlights": [
                "Implemented the Snapchat Lens feature, allowing millions of users to add filters to their photos and videos",
                "Created the Snapchat Lens Studio, allowing users to create their own lenses",
                "Migrated the codebase after the acquisition of Bitstrips, smoothly integrating Bitmoji",
                "Met LeBron James and Drake, and got a shoutout from Drake on his Snapchat story"
            ]
        }
    ]
}

Notice that the schema is a list of work positions. Each work position is a JSON with the fields of name, position, startDate, endDate, and highlights. The higlights are a list of strings. 

This is extremely flexible, as the following is also valid work JSON:
{
    "work": [
        {
            "company": "McKinsey & Company",
            "position": "Associate",
            "startDate": "January 2022",
            "endDate": "Present",
            "highlights": [
                "Consulting for ESG and sustainability for Fortune 500 companies",
                "Working in a dynamic team of 5 people"
            ]
        },
        {
            "company": "Harvard University Alumni Association",
            "position": "Alumni Relations Associate",
            "startDate": "January 2021",
            "endDate": "December 2021",
            "highlights": [
                "Secured funding of over 5 million dollars for the Harvard Alumni Association in order to secure e-mail addresses of all Harvard alumni"
            ]
        },
        {
            "company": "Phi Beta Kappa",
            "position": "President",
            "startDate": "January 2021",
            "endDate": "December 2021",
            "highlights": [
                "Organized community building events with members of the Cambridge community",
                "Chaired the Harvard pan-helenic council"
            ]
        }
    ]
}

Write the work section according to the schema. Include all work positions, but only the ones present in the CV. It is stricly important to include ONLY the work key in the top-level of the JSON. Please only include the work experience and no other data, as including other keys can hurt our applicants prospective job opportunities. Include only the JSON in your response.
"""