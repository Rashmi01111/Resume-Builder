# main.py

from models.generative_model import GenerativeModel
from utils.text_cleaner import clean_resume_text
from utils.resume_formatter import format_resume

def main():
    # Example user input
    name = "John Doe"
    job_title = "Software Engineer"

    # Initialize the generative model
    model = GenerativeModel()

    # Generate a resume using the pre-trained model
    resume_text = model.generate_resume(name, job_title)
    print("Generated Resume (Raw):")
    print(resume_text)

    # Clean the resume text to replace placeholders with user-friendly prompts
    cleaned_text = clean_resume_text(resume_text)
    formatted_resume = format_resume(cleaned_text)

    print("\nCleaned & Formatted Resume:")
    print(formatted_resume)

if __name__ == "__main__":
    main()
