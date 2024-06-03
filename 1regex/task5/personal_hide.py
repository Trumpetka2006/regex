import re


def phone_hide(persons: list[str]) -> list[str]:
    hiden = []
    for i in persons:
        hiden.append(re.sub(r"\d{3}\-\d{3}","***-***",i))

    return hiden


def email_hide(persons: list[str]) -> list[str]:
    hiden = []
    for i in persons:
        buffer=re.sub(r'(\w)(\S+)(\w)(@)', lambda m: f"{m.group(1)}***{m.group(3)}{m.group(4)}", i)
        hiden.append(re.sub(r"\@\w*(?=\w)","@***", buffer))

    print(hiden)
    return hiden
