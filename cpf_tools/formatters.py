"""
CPF formatting utilities.
"""
from typing import Union

__all__ = ["cpf_format"]


def cpf_format(cpf: Union[int, str, float]) -> str:
    """
    Format CPF.

    Args:
        cpf (Union[int, str, float]): CPF

    Returns:
        str: Formatted CPF "***.***.***-**"
    """
    try:
        if type(cpf) == float:
            cpf = int(cpf)
        cpf_cleaned = int(''.join(filter(str.isdigit, str(cpf))))
        cpf_cleaned = str(cpf_cleaned).zfill(11)
        return (f'{cpf_cleaned[:3]}.{cpf_cleaned[3:6]}.{cpf_cleaned[6:9]}-{cpf_cleaned[9:]}')
    except ValueError:
        return ''
