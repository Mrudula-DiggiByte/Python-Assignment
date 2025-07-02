from src.validating_email_addresses_with_a_filter.util import filter_mail
if __name__ == '__main__':
    n = int(input("Enter number of emails: "))
    emails = [input(f"Email {_+1}: ") for _ in range(n)]
    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print("Valid Emails:", filtered_emails)