def bytearrayToLettersAndNumbers(input: bytearray) -> str:
    AmountOfSymbols = 62
    AmountOfNumbers = 10
    AmountOfNumbersAndUppercaseLetters = 36
    FirstUtf8NumberPosition = 48
    FirstUtf8UppercaseLetterPosition = 65
    FirstUtf8LowercaseLetterPosition = 97
    output = ""
    for byte in input:
        letterUtf8Number = byte % AmountOfSymbols
        if letterUtf8Number < AmountOfNumbers:
            letterUtf8Number += FirstUtf8NumberPosition
        elif letterUtf8Number < AmountOfNumbersAndUppercaseLetters:
            letterUtf8Number -= AmountOfNumbers
            letterUtf8Number += FirstUtf8UppercaseLetterPosition
        else:
            letterUtf8Number -= AmountOfNumbersAndUppercaseLetters
            letterUtf8Number += FirstUtf8LowercaseLetterPosition
        output += str(chr(letterUtf8Number))

    return output


def bytearrayToLetters(input: bytearray) -> str:
    AmountOfSymbols = 52
    AmountOfUppercaseLetters = 26
    FirstUtf8UppercaseLetterPosition = 65
    FirstUtf8LowercaseLetterPosition = 97
    output = ""
    for byte in input:
        letterUtf8Number = byte % AmountOfSymbols
        if letterUtf8Number < AmountOfUppercaseLetters:
            letterUtf8Number += FirstUtf8UppercaseLetterPosition
        else:
            letterUtf8Number -= AmountOfUppercaseLetters
            letterUtf8Number += FirstUtf8LowercaseLetterPosition
        output += str(chr(letterUtf8Number))
    return output


def bytearrayToNumbers(input: bytearray) -> str:
    return str(int.from_bytes(input, "big"))[:len(input)]