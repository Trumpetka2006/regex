import re


def pick_numbers(text: str) -> list[str]:
    return re.split(r"[,\n]", text)
