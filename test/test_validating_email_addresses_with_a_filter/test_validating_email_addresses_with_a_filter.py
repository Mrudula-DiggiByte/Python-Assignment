import unittest
from src.validating_email_addresses_with_a_filter.util import filter_mail

class TestFilterMail(unittest.TestCase):

    def test_valid_emails(self):
        emails = [
            "user@example.com",
            "john_doe-123@domain.org",
            "hello-world@xyz.net"
        ]
        result = filter_mail(emails)
        self.assertEqual(sorted(result), sorted(emails))

    def test_invalid_emails(self):
        emails = [
            "invalid@domain",         # No TLD
            "bad@.com",               # Domain starts with dot
            "@nodomain.com",         # No local part
            "user@domain.corporate", # TLD too long
            "weird#char@domain.com"  # Invalid character '#'
        ]
        result = filter_mail(emails)
        self.assertEqual(result, [])

    def test_mixed_emails(self):
        emails = [
            "valid123@abc.com",
            "nope@domain.coooom",
            "right_mail@a1.org",
            "wrong..@bad.com",
            "cool-user@xyz.co"
        ]
        expected = ["valid123@abc.com", "right_mail@a1.org", "cool-user@xyz.co"]
        result = filter_mail(emails)
        self.assertEqual(sorted(result), sorted(expected))

    def test_edge_cases(self):
        emails = [
            "a@b.cd",  # shortest valid email
            "x" * 30 + "@domain.com",  # long local part
            "name@sub.domain.com"     # invalid due to subdomain
        ]
        expected = ["a@b.cd", "x" * 30 + "@domain.com"]
        result = filter_mail(emails)
        self.assertEqual(sorted(result), sorted(expected))

if __name__ == '__main__':
    unittest.main()
