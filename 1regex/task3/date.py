import re

def find_dates(text):
    date = re.findall(r"\d{2}\.\d*\.\d{4}", text)
    return date
