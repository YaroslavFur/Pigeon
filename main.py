from hashlib import sha256

from PasswordTypeCaseEnums import PasswordType, PasswordCase
from BytearrayToPassword import bytearrayToNumbers, bytearrayToLetters, bytearrayToLettersAndNumbers


def main():
    InputSecret = "c9c529b3dc782e27"
    InputServiceInfo = "info.loe.lviv.ua"
    InputUserInfo = "tapocki20"
    InputPasswordLen = 8
    InputPasswordType = PasswordType.LETTERS_AND_NUMBERS
    InputPasswordCase = PasswordCase.MIXEDCASE

    print("Input:")
    print("\nServiceInfo: " + InputServiceInfo + "\nUserInfo: " + InputUserInfo + "\nPasswordLen: " + str(InputPasswordLen))
    print("PasswordType: " + InputPasswordType.name + "\nPasswordCase: " + InputPasswordCase.name + "\n\n\n")

    if InputPasswordLen < 4 or InputPasswordLen > 32:
        print("PasswordLen must be between 4 and 32, not " + str(InputPasswordLen))
        return

    HashingInput = InputSecret + InputServiceInfo + InputUserInfo
    Password = ""

    IsPasswordGood = False
    while not IsPasswordGood:
        IsPasswordGood = True
        Password = HashingInput = bytearray(sha256(str(HashingInput).encode('utf-8')).digest())
        Password = Password[:InputPasswordLen]
        print("Generated password: ")
        print(Password)

        match InputPasswordType:
            case PasswordType.LETTERS_AND_NUMBERS:
                Password = bytearrayToLettersAndNumbers(Password)

                # if there's no any lowercase symbols or no any uppercase symbols or no any numbers in the password - make another password
                if (
                        (not any(symbol for symbol in Password if symbol.islower())) or
                        (not any(symbol for symbol in Password if symbol.isupper())) or
                        (not any(symbol for symbol in Password if symbol.isnumeric()))
                ):
                    IsPasswordGood = False
                    print("No lowercase/uppercase/numeric symbols in password \"" + Password + "\".\n" +
                          "Gotta make another password using " + str(HashingInput) + "\nas hashing input\n\n")
                    continue
            case PasswordType.LETTERS_ONLY:
                Password = bytearrayToLetters(Password)

                # if there's no any lowercase symbols or no any uppercase symbols in the password - make another password
                if (
                        (not any(symbol for symbol in Password if symbol.islower())) or
                        (not any(symbol for symbol in Password if symbol.isupper()))
                ):
                    IsPasswordGood = False
                    print("No lowercase/uppercase symbols in password \"" + Password + "\".\n" +
                          "Gotta make another password using " + str(HashingInput) + "\nas hashing input\n\n")
                    continue
            case PasswordType.NUMBERS_ONLY:
                Password = bytearrayToNumbers(Password)
            case _:
                print("Wrong InputPasswordType variable value")
                return

        match InputPasswordCase:
            case PasswordCase.MIXEDCASE:
                pass
            case PasswordCase.LOWERCASE:
                Password = Password.lower()
            case PasswordCase.UPPERCASE:
                Password = Password.upper()
            case _:
                print("Wrong InputPasswordCase variable value")
                return

    print("Final password: " + Password)


if __name__ == '__main__':
    main()