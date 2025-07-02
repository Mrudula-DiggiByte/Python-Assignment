import re
def is_valid_email(email):
    pattern = r"^[A-Za-z0-9_\-]+@[A-Za-z0-9]+\.[a-zA-Z]{1,3}$"
    return bool(re.match(pattern, email))
def filter_mail(emails):
    return list(filter(is_valid_email, emails))
