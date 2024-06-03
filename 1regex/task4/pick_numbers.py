import re


def pick_numbers(text: str) -> list[int]:
    rawnum = re.findall(r"\d+\s*\d*", text)
    print(rawnum)
    numbers = []
    for input_string in rawnum:
        #print(i)
        num = re.sub(r'\s+', '', input_string)
        print(num)
        numbers.append(int(num))


    return numbers
