from faker import Faker

fake = Faker()


def get_random_full_name():
    return fake.first_name()


def get_random_email():
    return fake.email()


def get_random_address():
    return fake.street_address()
