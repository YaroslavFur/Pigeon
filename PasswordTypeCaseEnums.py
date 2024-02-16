from enum import Enum


class PasswordType(Enum):
    LETTERS_AND_NUMBERS = 1
    LETTERS_ONLY = 2
    NUMBERS_ONLY = 3


class PasswordCase(Enum):
    MIXEDCASE = 1
    LOWERCASE = 2
    UPPERCASE = 3