from openai import OpenAI
import google.generativeai as genai
import json
from stqdm import stqdm
from logger import get_logger

# Setup module logger
logger = get_logger('prompt_engineering')

SYSTEM_PROMPT = "You are a smart assistant to career advisors at the Harvard Extension School. You will reply with JSON only."

CV_TEXT_PLACEHOLDER = "<CV_TEXT>"

SYSTEM_TAILORING = """
You are a smart assistant to career advisors at the Harvard Extension School. Your take is to rewrite
resumes to be more brief and convincing according to the Resumes and Cover Letters guide.
"""

TAILORING_PROMPT = """
Consider the following CV:
<CV_TEXT>

Your task is to rewrite the given CV. Follow these guidelines:
- Be truthful and objective to the experience listed in the CV
- Be specific rather than general
- Rewrite job highlight items using STAR methodology (but do not mention STAR explicitly)
- Fix spelling and grammar errors
- Write to express not impress
- Articulate and don't be flowery
- Prefer active voice over passive voice
- Do not include a summary about the candidate

Improved CV:
"""

BASICS_PROMPT = """
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

EDUCATION_PROMPT = """
You are going to write a JSON resume section for an applicant applying for job posts.

Consider the following CV:
<CV_TEXT>

Now consider the following TypeScript Interface for the JSON schema:

interface EducationItem {
    institution: string;
    area: string;
    additionalAreas: string[];
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

AWARDS_PROMPT = """
You are going to write a JSON resume section for an applicant applying for job posts.

Consider the following CV:
<CV_TEXT>

Now consider the following TypeScript Interface for the JSON schema:

interface AwardItem {
    title: string;
    date: string;
    awarder: string;
    summary: string;
}

interface Awards {
    awards: AwardItem[];
}

Write the awards section according to the Awards schema. Include only the awards section. On the response, include only the JSON.
"""

PROJECTS_PROMPT = """
You are going to write a JSON resume section for an applicant applying for job posts.

Consider the following CV:
<CV_TEXT>

Now consider the following TypeScript Interface for the JSON schema:

interface ProjectItem {
    name: string;
    description: string;
    keywords: string[];
    url: string;
}

interface Projects {
    projects: ProjectItem[];
}

Write the projects section according to the Projects schema. Include all projects, but only the ones present in the CV. On the response, include only the JSON.
"""

SKILLS_PROMPT = """
You are going to write a JSON resume section for an applicant applying for job posts.

Consider the following CV:
<CV_TEXT>

type HardSkills = "Programming Languages" | "Tools" | "Frameworks" | "Computer Proficiency";
type SoftSkills = "Team Work" | "Communication" | "Leadership" | "Problem Solving" | "Creativity";
type OtherSkills = string;

Now consider the following TypeScript Interface for the JSON schema:

interface SkillItem {
    name: HardSkills | SoftSkills | OtherSkills;
    keywords: string[];
}

interface Skills {
    skills: SkillItem[];
}

Write the skills section according to the Skills schema. Include only up to the top 4 skill names that are present in the CV and related with the education and work experience. On the response, include only the JSON.
"""

WORK_PROMPT = """
You are going to write a JSON resume section for an applicant applying for job posts.

Consider the following CV:
<CV_TEXT>

Now consider the following TypeScript Interface for the JSON schema:

interface WorkItem {
    company: string;
    position: string;
    startDate: string;
    endDate: string;
    location: string;
    highlights: string[];
}

interface Work {
    work: WorkItem[];
}

Write a work section for the candidate according to the Work schema. Include only the work experience and not the project experience. For each work experience, provide  a company name, position name, start and end date, and bullet point for the highlights. Follow the Harvard Extension School Resume guidelines and phrase the highlights with the STAR methodology
"""


def generate_json_resume(cv_text, model_type, api_model, api_key):
    """
    Generate a structured JSON resume from the input CV text.
    
    Args:
        cv_text: The text of the CV
        model_type: The type of LLM to use (OpenAI/Gemini)
        api_model: The specific model to use
        api_key: The API key for the LLM service
        
    Returns:
        A dictionary containing the structured resume
    """
    logger.info(f"Generating JSON resume using {model_type} model: {api_model}")
    logger.debug(f"CV text length: {len(cv_text)} characters")
    
    try:
        if model_type == "OpenAI":
            client = OpenAI(api_key=api_key)
            logger.debug(f"OpenAI client initialized")
            
            response = client.chat.completions.create(
                model=api_model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"Generate a JSON resume for the following CV:\n{cv_text}"},
                ],
                temperature=0.5,
                max_tokens=4000
            )
            logger.debug(f"OpenAI API call completed with {len(response.choices[0].message.content)} characters")
            
            response_content = response.choices[0].message.content
            
            # Extract JSON from the response
            try:
                resume_json = json.loads(response_content)
                logger.info("Successfully parsed JSON resume")
                return resume_json
            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse JSON response: {str(e)}")
                logger.debug(f"Response content: {response_content}")
                raise ValueError("Failed to generate valid JSON from the LLM response")
                
        elif model_type == "Gemini":
            logger.debug(f"Initializing Gemini with API key")
            genai.configure(api_key=api_key)
            
            model = genai.GenerativeModel(api_model)
            logger.debug(f"Gemini model initialized: {api_model}")
            
            response = model.generate_content(
                f"Generate a JSON resume for the following CV:\n{cv_text}"
            )
            logger.debug(f"Gemini API call completed")
            
            # Extract JSON from the response
            try:
                response_text = response.text
                logger.debug(f"Gemini response length: {len(response_text)} characters")
                
                # Find JSON content in response text
                start_idx = response_text.find('{')
                end_idx = response_text.rfind('}') + 1
                
                if start_idx >= 0 and end_idx > start_idx:
                    json_text = response_text[start_idx:end_idx]
                    resume_json = json.loads(json_text)
                    logger.info("Successfully parsed JSON resume from Gemini response")
                    return resume_json
                else:
                    logger.error("Failed to extract JSON from Gemini response")
                    raise ValueError("Could not find JSON content in Gemini response")
            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse JSON response from Gemini: {str(e)}")
                raise ValueError("Failed to generate valid JSON from the Gemini response")
        else:
            logger.error(f"Unsupported model type: {model_type}")
            raise ValueError(f"Unsupported model type: {model_type}")
            
    except Exception as e:
        logger.error(f"Error during JSON resume generation: {str(e)}", exc_info=True)
        raise

def tailor_resume(resume_json, job_description, model_type, api_model, api_key):
    """
    Tailor the resume to the given job description
    
    Args:
        resume_json: The structured resume data
        job_description: The job description text
        model_type: The type of LLM to use (OpenAI/Gemini)
        api_model: The specific model to use
        api_key: The API key for the LLM service
        
    Returns:
        The tailored resume JSON
    """
    logger.info(f"Tailoring resume to job description using {model_type} model: {api_model}")
    logger.debug(f"Job description length: {len(job_description)} characters")
    
    try:
        # Convert resume JSON to text for the tailoring process
        resume_text = json.dumps(resume_json, indent=2)
        
        if model_type == "OpenAI":
            client = OpenAI(api_key=api_key)
            logger.debug(f"OpenAI client initialized for tailoring")
            
            prompt = TAILORING_PROMPT.replace(CV_TEXT_PLACEHOLDER, resume_text)
            prompt += f"\n\nJob Description:\n{job_description}"
            
            response = client.chat.completions.create(
                model=api_model,
                messages=[
                    {"role": "system", "content": SYSTEM_TAILORING},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.5,
                max_tokens=4000
            )
            logger.debug(f"OpenAI tailoring API call completed")
            
            # Generate new JSON from the tailored content
            tailored_text = response.choices[0].message.content
            logger.debug(f"Tailored content received ({len(tailored_text)} characters)")
            
            # Now process the tailored text back into a JSON resume
            tailored_json = generate_json_resume(tailored_text, model_type, api_model, api_key)
            logger.info("Successfully converted tailored resume to JSON format")
            return tailored_json
            
        elif model_type == "Gemini":
            logger.debug(f"Initializing Gemini with API key for tailoring")
            genai.configure(api_key=api_key)
            
            model = genai.GenerativeModel(api_model)
            logger.debug(f"Gemini model initialized for tailoring: {api_model}")
            
            prompt = TAILORING_PROMPT.replace(CV_TEXT_PLACEHOLDER, resume_text)
            prompt += f"\n\nJob Description:\n{job_description}"
            
            response = model.generate_content(prompt)
            logger.debug(f"Gemini tailoring API call completed")
            
            # Generate new JSON from the tailored content
            tailored_text = response.text
            logger.debug(f"Tailored content received from Gemini ({len(tailored_text)} characters)")
            
            # Now process the tailored text back into a JSON resume
            tailored_json = generate_json_resume(tailored_text, model_type, api_model, api_key)
            logger.info("Successfully converted tailored Gemini resume to JSON format")
            return tailored_json
        else:
            logger.error(f"Unsupported model type for tailoring: {model_type}")
            raise ValueError(f"Unsupported model type: {model_type}")
            
    except Exception as e:
        logger.error(f"Error during resume tailoring: {str(e)}", exc_info=True)
        raise
