import re

def validate_phone(phone):
    pattern = r'^(\(\d{3}\)\s|\d{3}[-\s]?|\d{3})\d{3}[-\s]?\d{4}$'
    if re.match(pattern, phone):
        return True
    else:
        return False

def validate_ssn(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    if re.match(pattern, ssn):
        return True
    else:
        return False

def validate_zip(zip_code):
    pattern = r'^\d{5}(-\d{4})?$'
    if re.match(pattern, zip_code):
        return True
    else:
        return False

def main():
    phone = input('Enter your phone number: ')
    ssn = input('Enter your ssn: ')
    zip_code = input('Enter your zip code: ')

    if validate_phone(phone):
        print('Your phone number is valid')
    else:
        print('Your phone number is not valid')

    if validate_ssn(ssn):
        print('Your ssn is valid')
    else:
        print('Your ssn is not valid')

    if validate_zip(zip_code):
        print('Your zip code is valid')
    else:
        print('Your zip code is not valid')

main()
