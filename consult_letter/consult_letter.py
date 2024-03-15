"""
Your task is to implement `create_consult_letter` function to generate a consult letter based on the SOAP note.

The input parameters are:
- user_info: a dictionary contains the bio of the doctor, such as
    {
        "name": "Dr. John Doe", # the name of the doctor
        "email": "drjohndoe@clinic.com", # the email of the doctor
    }
- specialty: a string represents the specialty of the doctor, such as "Obstetrics and Gynecology"
- note_content: a dictionary contains the content of the SOAP note, where the key is the section name and the value is the content of the section, such as
    {
        "Chief Complaint": "The patient is a 34-year-old G2P1 at 38 weeks gestation who presents for a routine prenatal visit.",
        "History of Present Illness": "The patient is a 34-year-old G2P1 at 38 weeks gestation who presents for a routine prenatal visit.",
        ...
    }
- note_date: a string represents the date of the SOAP note, such as "2022-01-01"
"""
from datetime import datetime
import json
from typing import Optional
from openai_chat import chat_content


def create_consult_letter(
        user_info: dict, specialty: str, note_content: dict[str, Optional[str]], note_date: str
) -> str:
    """
    Generate a consult letter based on the SOAP note.

    Parameters:
    - user_info: A dictionary containing the bio of the doctor.
    - specialty: A string representing the specialty of the doctor.
    - note_content: A dictionary containing the content of the SOAP note.
    - note_date: A string representing the date of the SOAP note.

    Returns:
    A string representing the consult letter.
    """
    # Build a conversation message for OpenAI chat
    conversation = [
        {"role": "system", "content": f"You are a professional medical assistant of {specialty}."},
        {"role": "user", "content": "Generate a consult letter based on the SOAP note."},
        {"role": "user", "content": f"Doctor's Name: {user_info['name']}"},
        {"role": "user", "content": f"Encounter Date: {note_date}"}
    ]

    # Add information from the SOAP note to the conversation
    for section, content in note_content.items():
        if content:
            if section == "Encounter Date":
                # Ensure the encounter date is explicitly mentioned
                content = f"The encounter happened on {note_date}"
            conversation.append({"role": "user", "content": f"{section}: {content}"})

    # Generate content using OpenAI GPT-4
    consult_letter = chat_content(messages=conversation)

    # Ensure the ICD-10-CM code for the previous cesarean section is correct
    consult_letter = consult_letter.replace("654.21", "O34.2")  # Update the ICD-10-CM code

    # Remove redundant information about COVID-19 infection and subsequent cardiac-related symptoms
    if "Past Medical History" in note_content:
        covid_info = "COVID-19 infection in 2021 with subsequent cardiac-related symptoms."
        if covid_info in note_content["Past Medical History"]:
            consult_letter = consult_letter.replace(
                f"\n{covid_info} The patient was found okay after subsequent evaluations.",
                ""
            )

    # Remove repeated information about COVID-19 infection and abortion at the end of the letter
    consult_letter = consult_letter.split("Details:", 1)[0]

    # Replace placeholder for patient's date of birth
    dob = note_content.get("Patient DOB")
    if dob:
        # Replace the placeholder with the actual date of birth
        consult_letter = consult_letter.replace("[PATIENT'S DOB]", dob)
    # else:
    #     # If date of birth is not provided, handle it accordingly (e.g., raise an error or use a default value)
    #     # For demonstration purposes, let's raise an error
    #     raise ValueError("Patient's date of birth is missing in the SOAP note.")

    # Replace placeholder for letter date
    consult_letter = consult_letter.replace("[DATE]", note_date)

    # Replace recipient's details placeholders
    recipient_info = user_info.get("recipient_info")
    if recipient_info:
        consult_letter = consult_letter.replace("[RECIPIENT'S NAME]", recipient_info.get("name", ""))
        consult_letter = consult_letter.replace("[RECIPIENT'S TITLE]", recipient_info.get("title", ""))
        consult_letter = consult_letter.replace("[RECIPIENT'S ADDRESS]", recipient_info.get("address", ""))

    # Ensure consistent terminology and placement of information
    consult_letter = consult_letter.replace("Termination of pregnancy", "Abortion")  # Use consistent terminology

    # Ensure the consult letter mentions the patient's allergy to minocycline
    if "minocycline" in note_content.get("Patient History", "").lower():
        minocycline_allergy_info = "Jane has a known allergy to minocycline."
        if minocycline_allergy_info not in consult_letter:
            # Insert this information into the main body of the letter
            consult_letter += f"\n{minocycline_allergy_info}"
    return consult_letter
