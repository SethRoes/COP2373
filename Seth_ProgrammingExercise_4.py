import re

def validate_phone_number(phone_number):

    pattern = re.compile(r"^(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$")
    return bool(pattern.match(phone_number))

def validate_ssn(ssn):

    pattern = re.compile(r"^(?!000|666|9\d{2})\d{3}-(?!00)\d{2}-(?!0000)\d{4}$")
    return bool(pattern.match(ssn))

def validate_zip_code(zip_code):

    pattern = re.compile(r"^\d{5}(?:-\d{4})?$")
    return bool(pattern.match(zip_code))

def main():

    print("--- Input Validation Tool ---")

    # Phone Number
    phone_input = input("Enter a phone number (e.g., (123) 456-7890 or 123-456-7890 or 1234567890): ")
    if validate_phone_number(phone_input):
        print(f"'{phone_input}' is a VALID phone number.")
    else:
        print(f"'{phone_input}' is NOT a valid phone number.")

    # Printing the Social Security Number
    ssn_input = input("Enter a Social Security Number (e.g., 123-45-6789): ")
    if validate_ssn(ssn_input):
        print(f"'{ssn_input}' is a VALID Social Security Number.")
    else:
        print(f"'{ssn_input}' is NOT a valid Social Security Number.")

    # Printing the ZIP Code
    zip_input = input("Enter a ZIP code (e.g., 12345 or 12345-6789): ")
    if validate_zip_code(zip_input):
        print(f"'{zip_input}' is a VALID ZIP code.")
    else:
        print(f"'{zip_input}' is NOT a valid ZIP code.")

if __name__ == "__main__":
    main()