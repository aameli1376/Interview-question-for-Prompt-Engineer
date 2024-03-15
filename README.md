# Consult Letter Generation

This project generates a consult letter based on SOAP notes using OpenAI's GPT-4 model.

## Installation

To install the required Python libraries, run:
`pip install -r requirements.txt`


Make sure you have an OpenAI API key stored in a `.env` file and loaded into the code before running.

## Usage

### Generating Consult Letter

1. **Prepare Data**: Prepare the necessary input data including user information, SOAP note content, and note date.
2. **Generate Consult Letter**: Use the `create_consult_letter` function from the `consult_letter` module to generate the consult letter.
3. **Review and Verify**: Review the generated consult letter for accuracy and completeness. You can use the `print_letter.py` script to generate a sample output in email format (output saved in `generated_consult_letter.txt`).

### Running Tests

To run unit tests, use the following command. It passed most of the tests:
`python -m pytest .`

## Files

List of files in the package:

- `consult_letter.py`: Contains the `create_consult_letter` function to generate the consult letter based on SOAP notes.
- `openai_chat.py`: Provides the functionality to interact with OpenAI's GPT-4 model for generating text.
- `test_consult_letter.py`: Unit tests to verify the functionality of the `create_consult_letter` function.
- `print_letter.py`: Script to demonstrate the generation of a consult letter using sample data.

### Running print_letter.py
To run the print_letter.py to see the email-style consult letter, use the following command:
`python3 print_letter.py`

## Sample Usage

For a sample usage of the consult letter generation, refer to the `print_letter.py` script.

## Author

Ali Ameli

Data Scientist
