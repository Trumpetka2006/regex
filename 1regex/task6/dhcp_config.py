import re


def check_dhcp_config(line: str) -> bool:
    return bool( re.match(r"^\s{0}\w*\.\w*\.cz\s{1}ha=\w{12}\:ip=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\s{0}$", line))


def transfer_dhcp_config(text: str) -> str:
    re.sub()
    text = """
host cosi.kdesi.cz {
  link address 00:40:38:9a:5b:60;
    fix  address 192.51.38.444;
}
"""
    return text
