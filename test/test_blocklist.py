import approvaltests
import pytest

from wimp import Customer, Blocklist


@pytest.fixture
def blocklist():
    return Blocklist(emails=["email1"], phones=["phone1"])

def test_blocklisting_both_listed(blocklist):
    customer = Customer.with_email_and_phone("email1", "phone1")
    assert blocklist.is_restricted(customer)

def test_blocklisting_email_listed(blocklist):
    customer = Customer.with_email_and_phone("email1", "another_phone")
    assert blocklist.is_restricted(customer)

def test_blocklisting_phone_listed(blocklist):
    customer = Customer.with_email_and_phone("another_email", "phone1")
    assert blocklist.is_restricted(customer)

def test_blocklisting_nothing_listed(blocklist):
    customer = Customer.with_email_and_phone("another_email", "another_phone")
    assert not blocklist.is_restricted(customer)

def test_blocklisting():
    blocklist = Blocklist(emails=["email1"], phones=["phone1"])
    customers = [
        Customer.with_email_and_phone("email1", "phone1"),
        Customer.with_email_and_phone("email1", "another_phone"),
        Customer.with_email_and_phone("another_email", "phone1"),
        Customer.with_email_and_phone("another_email", "another_phone"),
    ]
    approvaltests.approvals.verify_all(f"Decide whether a customer is restricted\n according to Blocklist with contents {blocklist.emails} and {blocklist.phones}",
                                       [f"{c.email}, {c.phone} => {blocklist.is_restricted(c)}" for c in customers])
