"""
CPF Tools - Brazilian CPF (Cadastro de Pessoas Físicas) validation and formatting.

This package provides utilities for validating and formatting Brazilian CPF numbers.

Public API:
    - cpf_int_validation(cpf: int) -> bool: Validate CPF as integer
    - cpf_str_validation(cpf: str) -> bool: Validate CPF as string
    - cpf_format(cpf: Union[int, str, float]) -> str: Format CPF to "XXX.XXX.XXX-XX"

Usage:
    from cpf_tools import cpf_format, cpf_int_validation, cpf_str_validation

    # Validate integer CPF
    is_valid = cpf_int_validation(12345678909)

    # Validate string CPF
    is_valid = cpf_str_validation("123.456.789-09")

    # Format CPF
    formatted = cpf_format(12345678909)
"""

from .validators import cpf_int_validation, cpf_str_validation
from .formatters import cpf_format

__all__ = ["cpf_int_validation", "cpf_str_validation", "cpf_format"]
