from consult_letter import create_consult_letter

# Sample data for testing
user_info = {"name": "Dr. John Doe", "email": "drjohndoe@clinic.com"}
specialty = "Obstetrics & Gynecology (ObGyn)"
note_date = "2022/01/01"
note_content = {
    "Patient Name": "Betty",
    "Chief Complaint": "Ear pain",
    "History of Present Illness": "\n• Left-sided ear pain\n• No drainage noted\n• Intermittent hearing loss reported\n• Pain worsens with chewing\n• Inconsistent use of mouthpiece for teeth clenching\n• Pain relief when lying on contralateral side",
    "Social History": "\n• Occasional Reactive use for allergies\n• Allergy to salt",
    "The Review of Systems": "\n• Intermittent hearing loss\n• No swallowing issues\n• No nasal congestion\n• Allergies present, takes Reactive occasionally",
    "Current Medications": "\n• Reactive for allergies",
    "Allergies": "\n• Allergic to salt",
    "Physical Examination": "\n• Right ear canal clear\n• Right tympanic membrane intact\n• Right ear space aerated\n• Left ear canal normal\n• Left eardrum normal, no fluid or infection\n• Nose patent\n• Paranasal sinuses normal\n• Oral cavity clear\n• Tonsils absent\n• Good dentition\n• Pain along pterygoid muscles\n• Heart and lungs clear\n• No neck tenderness or lymphadenopathy",
    "Assessment and Plan": "Problem 1:\nEar pain\nDDx:\n• Temporomandibular joint disorder: Likely given the jaw pain, history of teeth clenching, and normal ear examination.\nPlan:\n- Ordered audiogram to check hearing\n- Advised to see dentist for temporomandibular joint evaluation\n- Recommended ibuprofen for pain\n- Suggested soft foods diet\n- Avoid chewing gum, hard candies, hard fruits, ice, and nuts\n- Follow-up if symptoms persist"
}

# Call the function
consult_letter = create_consult_letter(user_info, specialty, note_content, note_date)


# Print the result
print("Generated Consult Letter:")
print(consult_letter)
