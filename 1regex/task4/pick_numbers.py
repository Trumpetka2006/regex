import re


def pick_numbers(text: str) -> list[int]:
    rawnum = re.findall(r"\d*", text)
    numbers = []
    for i in rawnum:
        if i != '':
            numbers.append(int(i))

    return numbers
