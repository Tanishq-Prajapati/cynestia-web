import re

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
validate_phone_number_pattern = "^\\+?[1-9][0-9]{7,14}$"

# creating the valdiators for the fields of the Form in django
class Validators:
    def valdiate_full_name(self, name: str):
        if len(name.replace(" ","")) < 3:
            # error detected in the IF-STATEMENT
            return "Full-name should be atleast 3 characters long."
        return None
    
    def validate_email_id(self, email: str):
        if re.fullmatch(email_regex, email):
            return None
        return "please enter a valid email-id."
    
    def phone_number(self, number: str):
        if not number.startswith("+"):
            return "please add country-code before mobile-number."
        # now matching the regex here
        if not re.fullmatch(validate_phone_number_pattern, number):
            return "please enter a valid mobile number."
        return None
    
    def subject(self, sub: str):
        if len(sub.replace(" ","")) < 3:
            return "subject should be atleast 3 character long."
        return None