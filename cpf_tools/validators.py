"""
CPF validation functions.
"""
from .core import calculate_check_digits
from .formatters import cpf_format

__all__ = ["cpf_int_validation", "cpf_str_validation"]


def cpf_int_validation(cpf: int) -> bool:
    """
    Validation CPF integer.

    Args:
        cpf (int): CPF.

    Returns:
        bool: If CPF real True else False.
    """
    clean_cpf = str(cpf).zfill(11)
    digito_0, digito_1 = calculate_check_digits(clean_cpf)

    if ((int(clean_cpf[9]) == int(digito_0)) and (int(clean_cpf[10]) == int(digito_1))):
        return True
    else:
        return False


def cpf_str_validation(cpf: str) -> bool:
    """
    Validation CPF string

    Args:
        cpf (str): CPF.

    Returns:
        bool: If CPF real True else False.
    """
    clean_cpf = cpf_format(cpf).replace('.', '').replace('-', '')

    try:
        return cpf_int_validation(cpf=int(clean_cpf))
    except ValueError:
        print('ERROR: CPF entered is not a number, please review.')
        return False
