"""
Core utilities and algorithms for CPF validation and formatting.
"""


def calculate_check_digits(cpf_str: str) -> tuple:
    """
    Calculate the check digits (verifier digits) for a CPF.

    Args:
        cpf_str (str): 11-digit CPF string (already zero-padded).

    Returns:
        tuple: (first_digit, second_digit) - The two check digits.
    """
    digito = {}
    digito[0] = 0
    digito[1] = 0
    a = 10
    total = 0
    for c in range(0, 2):
        for i in range(0, (9 + c)):
            total = total + int(cpf_str[i]) * a
            a -= 1
        digito[f'total_{c}'] = total
        total_value = total % 11
        digito[c] = (int(11 - (total_value))
                     if total_value > 0 else total_value)
        if digito[c] >= 10:
            digito[c] = int(str(digito[c])[-1])
        a = 11
        total = 0
    return (digito[0], digito[1])
