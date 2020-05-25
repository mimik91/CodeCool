import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):

    new_id = []

    for _ in range(number_of_small_letters):
        string.ascii_lowercase
        small_letter = random.choice(string.ascii_lowercase)
        new_id.append(small_letter)

    for _ in range(number_of_capital_letters):
        string.ascii_uppercase
        capital_letter = random.choice(string.ascii_uppercase)
        new_id.append(capital_letter)

    for _ in range(number_of_digits):
        string.digits
        digit = random.choice(string.digits)
        new_id.append(digit)

    for _ in range(number_of_special_chars):
        special_chars = random.choice(allowed_special_chars)
        new_id.append(special_chars)

    random.shuffle(new_id)
    generated_id = ''.join(new_id)

    return generated_id
