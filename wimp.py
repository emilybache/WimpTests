from enum import Enum


class Order:
    @staticmethod
    def from_data(pizza_type, size, customer, delivery):
        return Order()

    def create(self):
        return "id"


class Customer:
    @staticmethod
    def with_name(name):
        return Customer()

    @staticmethod
    def with_email_and_phone(email, phone):
        customer = Customer()
        customer.email = email
        customer.phone = phone
        return customer


class Blocklist:
    def __init__(self, emails, phones):
        self.phones = phones
        self.emails = emails

    def is_restricted(self, customer):
        if customer.email in self.emails or customer.phone in self.phones:
            return True
        return False

class Delivery(Enum):
    Collection = 1