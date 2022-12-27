import re
import uuid
import os

class read_cheque():
    def __init__(self, text):
        self.text = text

    def parse(self):
        return{
            'date' : self.get_date(),
            'payee': self.get_payee(),
            'rupee_words': self.get_rupee_words(),
            'rupees': self.get_rupee(),
            'acc_no': self.get_accno(),
            'ifsc': self.get_ifsc()
           }

    def get_date(self):
        patteren ='Date:(.*)Pay'
        matches = re.findall(patteren, self.text, flags=re.DOTALL)
        if matches:
           return matches[0].strip()
    def get_payee(self):
        patteren = 'Pay(.*)OR'
        matches = re.findall(patteren, self.text, flags = re.DOTALL)
        if matches:
            return matches[0].strip()
    def get_rupee_words(self):
        pattern = 'Rupees(.*)only|...Only'
        matches = re.findall(pattern,self.text)
        if matches:
            return matches[0].strip()

    def get_rupee(self):
        pattern = 'z. (.*)'
        # A/c No. :(.*)'
        matches = re.findall(pattern,self.text)
        if matches:
            return matches[0].strip()

    def get_accno(self):
        pattern = 'A/c No. :(.*)'
        matches = re.findall(pattern, self.text)
        if matches:
            return matches[0].strip()

    def get_ifsc(self):
        pattern = 'CODE - (.*) Signature'
        matches = re.findall(pattern,self.text)
        if matches:
            return matches[0].strip()

