from pii_anonymizer.standalone.analyze.detectors.base_detector import BaseDetector
from pii_anonymizer.standalone.analyze.utils.regex import RegEx
import re


class ThaiIdDetector(BaseDetector):
    def __init__(self):
        self.name = "TH_ID"
        self.pattern = RegEx().extract_digit().num_occurrences(13).build()

    def get_name(self):
        return self.name

    def get_pattern(self):
        return self.pattern

    def validate(self, text):
        digits_text = "".join(re.findall(r"\b\d+\b", text))

        if len(digits_text) != 13:
            return False

        sum = 0
        for idx, character in enumerate(digits_text):
            if idx == 12:  # ignore checksum digit
                break
            sum += int(character) * (13 - idx)

        checkDigit = (11 - (sum % 11)) % 10
        if checkDigit != int(digits_text[-1]):
            return False

        return True