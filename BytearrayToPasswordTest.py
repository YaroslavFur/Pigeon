import unittest
import BytearrayToPassword


class BytearrayToLettersAndNumbersTesting(unittest.TestCase):
    def test_main(self):
        AllLettersAndNumbers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        Input = bytearray(62 * 4)
        for i in range(0, 62 * 4):
            Input[i] = i
        Output = BytearrayToPassword.bytearrayToLettersAndNumbers(Input)
        for i in range(0, len(AllLettersAndNumbers)):
            if Output.count(AllLettersAndNumbers[i]) != 4:
                self.fail()
        for i in range(0, 62 * 4):
            if not Output[i] in AllLettersAndNumbers:
                self.fail()
        self.assertEqual(1, 1)


class BytearrayToLettersTesting(unittest.TestCase):
    def test_main(self):
        AllLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        Input = bytearray(52 * 4)
        for i in range(0, 52 * 4):
            Input[i] = i
        Output = BytearrayToPassword.bytearrayToLetters(Input)
        for i in range(0, len(AllLetters)):
            if Output.count(AllLetters[i]) != 4:
                self.fail()
        for i in range(0, 52 * 4):
            if not Output[i] in AllLetters:
                self.fail()
        self.assertEqual(1, 1)


class BytearrayToNumbersTesting(unittest.TestCase):
    def test_main(self):
        AllNumbers = "0123456789"
        Input = bytearray(10 * 25)
        for i in range(0, 10 * 25):
            Input[i] = i
        Output = BytearrayToPassword.bytearrayToNumbers(Input)
        for i in range(0, len(AllNumbers)):
            if Output.count(AllNumbers[i]) == 0:
                self.fail()
        for i in range(0, 10 * 25):
            if not Output[i] in AllNumbers:
                self.fail()
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
