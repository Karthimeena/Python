import re

class read_micr():
    def __init__(self, text):
        self.text = text

    def parse(self):
        return {
            'cheque_no': self.get_chequeno(),
            'micr_no': self.get_micr(),
            'acc_id': self.get_accid()
        }

    def get_chequeno(self):
        pattern = 'c(.*)c'
        matches = re.findall(pattern,self.text)
        if matches:
            return matches[0].strip()

    def get_micr(self):
        pattern = '(\d{9})08'
        matches = re.findall(pattern, self.text)
        if matches:
            return matches[0].strip()

    def get_accid(self):
        pattern = ' (\d{6})80'
        matches = re.findall(pattern, self.text)
        if matches:
            return matches[0].strip()

    def return_value(matches):
        if matches:
            return matches[0].strip()



