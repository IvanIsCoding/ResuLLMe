education_prompt = """
You are a career adviser at the Harvard Extension School. You are going to write a JSON resume section for an applicant applying for the following job post:
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

Write the education section according to the schema
"""