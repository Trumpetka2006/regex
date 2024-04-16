import re


def phone_hide(persons: list[str]) -> list[str]:
    hiden = []
    for i in persons:
        hiden.append(re.sub(r"\d{3}\-\d{3}","***-***",i))

    return hiden


def email_hide(persons: list[str]) -> list[str]:
    hiden = []
    for i in persons:
        buffer=re.sub(r"\@\w*(?=\w)","@***", i)
        hiden.append(re.sub(r"(?<=\S)\S*\@","***@" , buffer))

    print(hiden)
    return hiden
